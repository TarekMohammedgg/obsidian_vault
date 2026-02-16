

```dart 
import 'dart:convert';
import 'dart:developer';
import 'package:dio/dio.dart';
import 'package:gdrive_tutorial/auth_client.dart';
import 'package:gdrive_tutorial/gapi_constatns.dart';
import 'package:gdrive_tutorial/shared_prefs.dart';

class GoogleSheetsManager {
  late final Dio dio;
  final AuthClient authClient;

  // Internal variable to hold the token so we don't pass it around manually
  String? _currentAccessToken;
  bool _isRefreshing = false;

  GoogleSheetsManager({required this.authClient}) {
    _setupDio();
  }

  void _setupDio() {
    dio = Dio(
      BaseOptions(
        connectTimeout: const Duration(seconds: 30),
        receiveTimeout: const Duration(seconds: 30),
        // Set default headers applicable to most requests here
        headers: {
          GoogleApiConstants.headerContentType: GoogleApiConstants.mimeTypeJson,
        },
      ),
    );

    // Using QueuedInterceptorsWrapper to handle concurrency safely
    dio.interceptors.add(
      QueuedInterceptorsWrapper(
        // 1. ON REQUEST: Auto-inject the token
        onRequest: (options, handler) async {
          // If memory is empty, try to load from cache
          _currentAccessToken ??= await CacheHelper.getData("AccessToken");

          if (_currentAccessToken != null) {
            options.headers[GoogleApiConstants.headerAuthorization] =
                GoogleApiConstants.getBearerToken(_currentAccessToken!);
          }
          return handler.next(options);
        },

        // 2. ON ERROR: Handle 401 Silent Refresh
        onError: (DioException e, handler) async {
          if (e.response?.statusCode == 401) {
            // ✅ Prevent multiple simultaneous refreshes
            if (_isRefreshing) {
              log('⏳ Already refreshing token, waiting...');
              await Future.delayed(Duration(milliseconds: 500));
              return handler.next(e);
            }

            _isRefreshing = true;
            log('⚠️ Token expired (401). Attempting silent refresh...');

            try {
              final account = await authClient.attemptSilentSignIn();

              if (account != null && authClient.auth != null) {
                final newToken = authClient.auth!.accessToken;

                if (newToken.isNotEmpty) {
                  log('✅ Token refreshed successfully');

                  // Update local state and Cache
                  _currentAccessToken = newToken;
                  await CacheHelper.saveData("AccessToken", newToken);

                  // Update the failed request's header with the new token
                  e.requestOptions.headers[GoogleApiConstants
                      .headerAuthorization] = GoogleApiConstants.getBearerToken(
                    newToken,
                  );

                  // RETRY the request using the SAME dio instance
                  final response = await dio.fetch(e.requestOptions);

                  // Return the successful response to the original caller
                  return handler.resolve(response);
                } else {
                  log('❌ Access token is empty');
                  await CacheHelper.removeData("AccessToken");
                }
              } else {
                log('❌ Silent refresh returned null - session expired');
                await CacheHelper.removeData("AccessToken");
              }
            } catch (refreshError) {
              log('❌ Silent refresh failed: $refreshError');
              await CacheHelper.removeData("AccessToken");
            } finally {
              _isRefreshing = false; // ✅ Always unlock
            }
          }
          // Propagate the error if it wasn't a 401 or if refresh failed
          return handler.next(e);
        },
      ),
    );
  }

  /// Search for a spreadsheet by name in Google Drive
  Future<String?> findSpreadsheetByName({
    required String spreadsheetName,
  }) async {
    try {
      String query = GoogleApiConstants.buildSpreadsheetQuery(spreadsheetName);

      final response = await dio.get(
        GoogleApiConstants.driveFiles,
        queryParameters: {
          GoogleApiConstants.queryParamQ: query,
          GoogleApiConstants.queryParamFields: 'files(id, name)',
        },
      );

      if (response.statusCode == 200 && response.data['files'] != null) {
        final files = response.data['files'] as List;
        for (var file in files) {
          if (file['name'] == spreadsheetName) {
            CacheHelper.saveData("SpreadSheetId", file['id']);
            log(
              'Found existing spreadsheet: ${file['name']} (ID: ${file['id']})',
            );
            return file['id'];
          }
        }
      }

      log('Spreadsheet "$spreadsheetName" not found');
      return null;
    } catch (e) {
      log('Error finding spreadsheet: $e');
      return null;
    }
  }

  /// Create a new spreadsheet with specified sheet name
  Future<String?> createSpreadsheet({
    required String spreadsheetName,
    String sheetName = 'Sheet1',
  }) async {
    try {
      final spreadsheetData = {
        'properties': {'title': spreadsheetName},
        'sheets': [
          {
            'properties': {'title': sheetName},
          },
        ],
      };

      final response = await dio.post(
        GoogleApiConstants.createSpreadsheet,
        data: jsonEncode(spreadsheetData),
      );

      if (response.statusCode == 200) {
        String spreadsheetId = response.data['spreadsheetId'];
        CacheHelper.saveData("SpreadSheetId", spreadsheetId);
        log('Spreadsheet created: $spreadsheetName (ID: $spreadsheetId)');
        return spreadsheetId;
      }
      return null;
    } catch (e) {
      log('Error creating spreadsheet: $e');
      return null;
    }
  }

  /// Get or create spreadsheet helper
  Future<String?> getOrCreateSpreadsheet({
    required String spreadsheetName,
    String sheetName = 'Sheet1',
  }) async {
    log('Looking for spreadsheet: "$spreadsheetName"');

    String? spreadsheetId = await findSpreadsheetByName(
      spreadsheetName: spreadsheetName,
    );

    if (spreadsheetId == null) {
      log('Creating new spreadsheet: "$spreadsheetName"');
      spreadsheetId = await createSpreadsheet(
        spreadsheetName: spreadsheetName,
        sheetName: sheetName,
      );
    }
    return spreadsheetId;
  }

  /// Insert column headers (first row)
  Future<bool> insertHeaders({
    required String spreadsheetId,
    required List<String> headers,
    String sheetName = 'Sheet1',
  }) async {
    try {
      final range = '$sheetName!A1';
      final valueRange = {
        'range': range,
        'majorDimension': 'ROWS',
        'values': [headers],
      };

      final response = await dio.put(
        GoogleApiConstants.getSheetValues(spreadsheetId, range),
        queryParameters: {
          GoogleApiConstants.queryParamValueInputOption:
              GoogleApiConstants.valueInputOptionRaw,
        },
        data: jsonEncode(valueRange),
      );

      return response.statusCode == 200;
    } catch (e) {
      log('Error inserting headers: $e');
      return false;
    }
  }

  /// Insert data (append new row)
  Future<bool> insertData({
    required String spreadsheetId,
    required Map<String, dynamic> data,
    required List<String> columnHeaders,
    String sheetName = 'Sheet1',
  }) async {
    try {
      // Map data to the correct column order
      List<dynamic> rowData = [];
      for (String header in columnHeaders) {
        rowData.add(data[header] ?? '');
      }

      final range = '$sheetName!${GoogleApiConstants.defaultRangeFromA}';
      final valueRange = {
        'range': range,
        'majorDimension': 'ROWS',
        'values': [rowData],
      };

      final response = await dio.post(
        GoogleApiConstants.appendSheetValues(spreadsheetId, range),
        queryParameters: {
          GoogleApiConstants.queryParamValueInputOption:
              GoogleApiConstants.valueInputOptionUserEntered,
          GoogleApiConstants.queryParamInsertDataOption:
              GoogleApiConstants.insertDataOptionInsertRows,
        },
        data: jsonEncode(valueRange),
      );

      return response.statusCode == 200;
    } catch (e) {
      log('Error inserting data: $e');
      return false;
    }
  }

  /// Get all data from sheet
  Future<List<Map<String, dynamic>>?> getAllData({
    required String spreadsheetId,
    String sheetName = 'Sheet1',
  }) async {
    try {
      final range = '$sheetName!${GoogleApiConstants.defaultRangeAllColumns}';

      final response = await dio.get(
        GoogleApiConstants.getSheetValues(spreadsheetId, range),
      );

      if (response.statusCode == 200) {
        final values = response.data['values'] as List?;
        if (values == null || values.isEmpty) {
          log('No data found');
          return [];
        }

        // First row is headers
        List<String> headers = List<String>.from(values[0]);
        List<Map<String, dynamic>> result = [];

        for (int i = 1; i < values.length; i++) {
          Map<String, dynamic> row = {};
          List rowData = values[i];
          for (int j = 0; j < headers.length; j++) {
            row[headers[j]] = j < rowData.length ? rowData[j] : '';
          }
          result.add(row);
        }
        log('Retrieved ${result.length} rows');
        return result;
      }
      return null;
    } catch (e) {
      log('Error getting data: $e');
      return null;
    }
  }

  /// Update data in a specific row
  Future<bool> updateData({
    required String spreadsheetId,
    required int rowIndex, // 1-based index
    required Map<String, dynamic> data,
    required List<String> columnHeaders,
    String sheetName = 'Sheet1',
  }) async {
    try {
      List<dynamic> rowData = [];
      for (String header in columnHeaders) {
        rowData.add(data[header] ?? '');
      }

      final range = '$sheetName!A$rowIndex';
      final valueRange = {
        'range': range,
        'majorDimension': 'ROWS',
        'values': [rowData],
      };

      final response = await dio.put(
        GoogleApiConstants.getSheetValues(spreadsheetId, range),
        queryParameters: {
          GoogleApiConstants.queryParamValueInputOption:
              GoogleApiConstants.valueInputOptionUserEntered,
        },
        data: jsonEncode(valueRange),
      );

      if (response.statusCode == 200) {
        log('Data updated successfully at row $rowIndex');
        return true;
      }
      return false;
    } catch (e) {
      log('Error updating data: $e');
      return false;
    }
  }

  /// Delete a row (by clearing its content and shifting rows up)
  Future<bool> deleteRow({
    required String spreadsheetId,
    required int rowIndex, // 0-based index for API
    String sheetName = 'Sheet1',
  }) async {
    try {
      // 1. Get the Sheet ID first
      final sheetId = await _getSheetId(
        spreadsheetId: spreadsheetId,
        sheetName: sheetName,
      );

      if (sheetId == null) {
        log('Could not find sheet ID');
        return false;
      }

      // 2. Perform Batch Update to delete dimension
      final batchUpdateRequest = {
        'requests': [
          {
            'deleteDimension': {
              'range': {
                'sheetId': sheetId,
                'dimension': 'ROWS',
                'startIndex': rowIndex,
                'endIndex': rowIndex + 1,
              },
            },
          },
        ],
      };

      final response = await dio.post(
        GoogleApiConstants.batchUpdateSpreadsheet(spreadsheetId),
        data: jsonEncode(batchUpdateRequest),
      );

      if (response.statusCode == 200) {
        log('Row $rowIndex deleted successfully');
        return true;
      }
      return false;
    } catch (e) {
      log('Error deleting row: $e');
      return false;
    }
  }

  /// Helper: Get sheet ID by sheet name
  Future<int?> _getSheetId({
    required String spreadsheetId,
    required String sheetName,
  }) async {
    try {
      final response = await dio.get(
        GoogleApiConstants.getSpreadsheet(spreadsheetId),
        queryParameters: {
          GoogleApiConstants.queryParamFields:
              'sheets(properties(sheetId,title))',
        },
      );

      if (response.statusCode == 200) {
        final sheets = response.data['sheets'] as List;
        for (var sheet in sheets) {
          if (sheet['properties']['title'] == sheetName) {
            return sheet['properties']['sheetId'];
          }
        }
      }
      return null;
    } catch (e) {
      log('Error getting sheet ID: $e');
      return null;
    }
  }

  /// Clear all data (except headers)
  Future<bool> clearAllData({
    required String spreadsheetId,
    String sheetName = 'Sheet1',
  }) async {
    try {
      final range = '$sheetName!${GoogleApiConstants.defaultDataStartRow}';

      final response = await dio.post(
        GoogleApiConstants.clearSheetValues(spreadsheetId, range),
      );

      if (response.statusCode == 200) {
        log('All data cleared successfully');
        return true;
      }
      return false;
    } catch (e) {
      log('Error clearing data: $e');
      return false;
    }
  }
}

```