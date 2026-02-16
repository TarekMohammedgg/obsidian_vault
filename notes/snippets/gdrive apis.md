

```dart 
import 'dart:convert';
import 'dart:developer';
import 'dart:io';
import 'package:dio/dio.dart';
import 'package:http_parser/http_parser.dart' show MediaType;
import 'package:mime_type/mime_type.dart';

// Ensure these match your project structure
import 'package:gdrive_tutorial/gapi_constatns.dart';
import 'package:gdrive_tutorial/auth_client.dart';
import 'package:gdrive_tutorial/shared_prefs.dart';

class GdriveUpload {
  late final Dio dio;
  final AuthClient authClient;
  String? _currentAccessToken;
  bool _isRefreshing = false;

  // Public variable to store link after upload
  String? sharedFileLink;

  GdriveUpload({required this.authClient}) {
    _setupDio();
  }
  void _setupDio() {
    dio = Dio(
      BaseOptions(
        connectTimeout: const Duration(
          seconds: 60,
        ), // Increased for file uploads
        receiveTimeout: const Duration(seconds: 60),
      ),
    );
    dio.interceptors.add(
      QueuedInterceptorsWrapper(
        // 1. Auto-inject Token
        onRequest: (options, handler) async {
          _currentAccessToken ??= await CacheHelper.getData("AccessToken");
          if (_currentAccessToken != null) {
            options.headers[GoogleApiConstants.headerAuthorization] =
                GoogleApiConstants.getBearerToken(_currentAccessToken!);
          }
          return handler.next(options);
        },
        // 2. Auto-Refresh on 401
        onError: (DioException e, handler) async {
          if (e.response?.statusCode == 401) {
            // ✅ Prevent multiple simultaneous refreshes
            if (_isRefreshing) {
              log('⏳ Already refreshing token, waiting...');
              await Future.delayed(Duration(milliseconds: 500));
              return handler.next(e);
            }
            _isRefreshing = true;
            log('⚠️ Token expired. Attempting silent refresh...');
            try {
              final account = await authClient.attemptSilentSignIn();
              if (account != null && authClient.auth != null) {
                // ✅ v7.2.0: Get accessToken from GoogleSignInClientAuthorization
                final newToken = authClient.auth!.accessToken;

                if (newToken.isNotEmpty) {
                  log('✅ Token refreshed successfully');
                  // Update instance variable
                  _currentAccessToken = newToken;
                  // Save to cache
                  await CacheHelper.saveData("AccessToken", newToken);
                  // Update request header
                  e.requestOptions.headers[GoogleApiConstants
                      .headerAuthorization] = GoogleApiConstants.getBearerToken(
                    newToken,
                  );
                  // Retry the request
                  final response = await dio.fetch(e.requestOptions);
                  return handler.resolve(response);
                } else {
                  log('❌ Access token is null or empty');
                  await CacheHelper.removeData("AccessToken");
                }
              } else {
                log('❌ Silent refresh returned null - session expired');
                // Clear cache and require manual login
                await CacheHelper.removeData("AccessToken");
              }
            } catch (error) {
              log('❌ Refresh failed: $error');
              await CacheHelper.removeData("AccessToken");
            } finally {
              _isRefreshing = false; // ✅ Always unlock
            }
          }
          return handler.next(e);
        },
      ),
    );
  }

  // ---------------------------------------------------------------------------
  // BUSINESS METHODS
  // (No longer require 'accessToken' param)
  // ---------------------------------------------------------------------------

  Future<String?> findFolderByName({
    required String folderName,
    String? parentId,
  }) async {
    try {
      String query = GoogleApiConstants.buildFolderQuery(
        folderName,
        parentId: parentId,
      );

      final response = await dio.get(
        GoogleApiConstants.driveFiles,
        queryParameters: {
          GoogleApiConstants.queryParamQ: query,
          GoogleApiConstants.queryParamFields: 'files(id, name)',
        },
      );

      if (response.statusCode == 200 &&
          response.data['files'] != null &&
          response.data['files'].isNotEmpty) {
        final files = response.data['files'] as List;
        for (var file in files) {
          if (file['name'] == folderName) {
            log('Found existing folder: ${file['name']} (ID: ${file['id']})');
            return file['id'];
          }
        }
      }
      return null;
    } catch (e) {
      log('Error finding folder: $e');
      return null;
    }
  }

  Future<String?> createFolder({
    required String folderName,
    String? parentId,
  }) async {
    try {
      final folderMetadata = {
        'name': folderName,
        'mimeType': GoogleApiConstants.mimeTypeFolder,
        if (parentId != null) 'parents': [parentId],
      };

      final response = await dio.post(
        GoogleApiConstants.driveFiles,
        data: jsonEncode(folderMetadata),
        options: Options(
          // Only Content-Type needed, Auth is handled by Interceptor
          headers: {
            GoogleApiConstants.headerContentType:
                GoogleApiConstants.mimeTypeJson,
          },
        ),
      );

      if (response.statusCode == 200) {
        log(
          'Folder created: ${response.data['name']} (ID: ${response.data['id']})',
        );
        return response.data['id'];
      }
      return null;
    } catch (e) {
      log('Error creating folder: $e');
      return null;
    }
  }

  Future<String?> createOrFindFolder({
    required String folderName,
    String? parentId,
  }) async {
    // Attempt find
    String? folderId = await findFolderByName(
      folderName: folderName,
      parentId: parentId,
    );

    // If not found, create
    folderId ??= await createFolder(folderName: folderName, parentId: parentId);

    return folderId;
  }

  Future<void> uploadFile({
    required File file,
    required String folderName,
  }) async {
    // 1. Ensure folder exists
    String? folderId = await createOrFindFolder(folderName: folderName);

    if (folderId == null) {
      log('Failed to get or create folder, aborting upload.');
      return;
    }

    String fileName = file.path.split('/').last;
    String? mimeType = mime(fileName);

    // 2. Prepare Metadata and File for Multipart Upload
    final fileMetadata = {
      'name': fileName,
      'parents': [folderId],
      'mimeType': mimeType ?? GoogleApiConstants.mimeTypeOctetStream,
    };

    final formData = FormData.fromMap({
      'metadata': MultipartFile.fromString(
        jsonEncode(fileMetadata),
        contentType: MediaType.parse(GoogleApiConstants.mimeTypeJsonUtf8),
      ),
      'file': await MultipartFile.fromFile(
        file.path,
        filename: fileName,
        contentType: MediaType.parse(
          mimeType ?? GoogleApiConstants.mimeTypeOctetStream,
        ),
      ),
    });

    try {
      // 3. Execute Upload
      final response = await dio.post(
        GoogleApiConstants.driveUploadMultipart,
        data: formData,
        options: Options(
          // We must specify Multipart Related here
          headers: {
            GoogleApiConstants.headerContentType:
                GoogleApiConstants.mimeTypeMultipartRelated,
          },
        ),
        onSendProgress: (sent, total) {
          if (total > 0) {
            log('Upload Progress: ${(sent / total * 100).toStringAsFixed(0)}%');
          }
        },
      );

      if (response.statusCode == 200) {
        log('Upload successful: ${response.data}');
        String fileId = response.data['id'];
        sharedFileLink = GoogleApiConstants.getDriveFileLink(fileId);
        log('File ID: $fileId');
      } else {
        log('Upload failed with status: ${response.statusCode}');
      }
    } catch (e) {
      log('Upload Error: $e');
    }
  }

  Future<String> getfileSharedLink() async {
    return sharedFileLink ?? "not shared yet!";
  }
}

```