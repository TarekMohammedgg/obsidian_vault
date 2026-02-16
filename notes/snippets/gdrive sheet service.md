
```dart 
import 'dart:io';
import 'dart:convert' show jsonEncode, jsonDecode;
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:device_info_plus/device_info_plus.dart';
import 'package:google_sign_in/google_sign_in.dart';
import 'package:http/http.dart' as http;

/// ============================================================================
/// GOOGLE DRIVE & SHEETS SERVICE - PRODUCTION READY WITH MULTI-DEVICE MANAGEMENT
/// ============================================================================
///
/// This comprehensive service provides:
///
/// 🔐 **AUTHENTICATION & SESSION MANAGEMENT**
///    - Google OAuth 2.0 authentication
///    - Single-device session enforcement via Firebase Firestore
///    - Automatic device conflict detection and resolution
///    - Session tracking with device name and login time
///    - Automatic retry with exponential backoff for transient errors
///
/// 📁 **GOOGLE DRIVE INTEGRATION**
///    - Upload files to Google Drive
///    - Create and manage folders
///    - Make files publicly accessible
///    - Generate shareable Drive URLs
///    - Support for multiple file types (images, PDFs, documents)
///
/// 📊 **GOOGLE SHEETS INTEGRATION**
///    - Create and manage spreadsheets
///    - Add/read data from sheets
///    - Auto-format headers (bold, frozen row)
///    - Batch operations support
///    - Product database management
///
/// 🔄 **MULTI-DEVICE SESSION MANAGEMENT**
///    - Enforces single-device login per account
///    - Stores active session info in Firebase Firestore
///    - Tracks device ID, device name, and login time
///    - Prevents concurrent logins from multiple devices
///    - Automatic session cleanup on logout
///    - Polling mechanism for waiting on device conflicts
///
/// 🛡️ **ERROR HANDLING & RESILIENCE**
///    - Automatic retry with exponential backoff (1s → 2s → 4s)
///    - Handles Firestore unavailability gracefully
///    - Structured error responses (SignInResult)
///    - Comprehensive logging for debugging
///    - Transient error detection and recovery
///
/// 📱 **DEVICE INFORMATION**
///    - Unique device ID generation (Android/iOS)
///    - Device name retrieval (brand + model)
///    - Cross-platform support
///
/// REQUIRED PACKAGES:
///
/// Add these to your pubspec.yaml dependencies:
/// ```yaml
/// dependencies:
///   google_sign_in: ^6.2.1        # OAuth 2.0 authentication
///   http: ^1.6.0                  # HTTP requests to Google APIs
///   uuid: ^4.0.0                  # Generate unique IDs for products
///   cloud_firestore: ^4.0.0       # Firebase Firestore for session management
///   device_info_plus: ^9.0.0      # Device information
///   firebase_core: ^2.0.0         # Firebase initialization
/// ```
///
/// FIREBASE SETUP:
///
/// 1. FIREBASE PROJECT SETUP:
///    - Go to: https://console.firebase.google.com/
///    - Create a new project or select existing
///    - Add your Android/iOS app
///    - Download google-services.json (Android) or GoogleService-Info.plist (iOS)
///    - Enable Firestore Database in Firebase Console
///
/// 2. FIRESTORE SECURITY RULES:
///    ```
///    rules_version = '2';
///    service cloud.firestore {
///      match /databases/{database}/documents {
///        match /user_sessions/{email} {
///          allow read, write: if request.auth != null;
///        }
///      }
///    }
///    ```
///
/// GOOGLE CLOUD CONSOLE SETUP:
///
/// 1. ENABLE APIS:
///    - Go to: https://console.cloud.google.com/
///    - Create a new project or select existing
///    - Enable APIs & Services:
///      * Google Drive API
///      * Google Sheets API
///
/// 2. OAUTH 2.0 CLIENT ID:
///    - Go to: Credentials → Create Credentials → OAuth 2.0 Client ID
///    - Select: Android
///    - Package Name: com.example.gsheet_demo
///    - SHA-1 Fingerprint: Run `./gradlew signingReport` in android/
///
/// 3. OAUTH CONSENT SCREEN:
///    - Must be in Production mode (verified)
///    - Scopes: Drive + Sheets
///
/// USAGE EXAMPLE:
///
/// ```dart
/// final service = GDriveSheetService();
///
/// // Sign in with device conflict handling
/// final result = await service.handleSignIn();
/// if (result.success) {
///   print('Signed in successfully!');
/// } else if (result.isDeviceConflict) {
///   print('Device conflict: \${result.conflictingDeviceName}');
///   // Show waiting dialog or handle conflict
/// }
///
/// // Upload file to Drive
/// final url = await service.uploadFile(imageFile);
///
/// // Add data to Google Sheet
/// await service.addProductToSheet(
///   id: 'uuid',
///   productName: 'Product',
///   price: '99.99',
///   quantity: '10',
///   imageUrl: url,
/// );
///
/// // Sign out (cleans up Firestore session)
/// await service.signOut();
/// ```
///
/// ============================================================================

// ============================================================================
// CONSTANTS - Configuration values used throughout the service
// ============================================================================

/// OAuth 2.0 Scopes
class _Scopes {
  static const drive = 'https://www.googleapis.com/auth/drive';
  static const spreadsheets = 'https://www.googleapis.com/auth/spreadsheets';
}

/// Google Drive API Endpoints
class _DriveEndpoints {
  static const baseUrl = 'https://www.googleapis.com/drive/v3';
  static const uploadUrl = 'https://www.googleapis.com/upload/drive/v3';

  static String files() => '\$baseUrl/files';
  static String fileUpload(String fileId) =>
      '\$uploadUrl/files/\$fileId?uploadType=media';
  static String permissions(String fileId) =>
      '\$baseUrl/files/\$fileId/permissions';
  static String search(String query) =>
      '\$baseUrl/files?q=\$query&spaces=drive&pageSize=1';
}

/// Google Sheets API Endpoints
class _SheetsEndpoints {
  static const baseUrl = 'https://sheets.googleapis.com/v4/spreadsheets';

  static String create() => baseUrl;
  static String values(String spreadsheetId, String range) =>
      '\$baseUrl/\$spreadsheetId/values/\$range';
  static String append(String spreadsheetId, String range) =>
      '\$baseUrl/\$spreadsheetId/values/\$range:append?valueInputOption=RAW';
  static String batchUpdate(String spreadsheetId) =>
      '\$baseUrl/\$spreadsheetId:batchUpdate';
}

/// Default folder and file names
class _Defaults {
  static const driveFolderName = 'FlutterTest';
  static const spreadsheetName = 'FlutterTestDB';
  static const sheetName = 'Products';
}

/// Google Drive URL formats
class _DriveUrls {
  /// Opens file in Google Drive viewer (clickable in sheets)
  static String viewer(String fileId) =>
      'https://drive.google.com/file/d/\$fileId/view?usp=sharing';

  /// Direct download URL (for programmatic access)
  static String download(String fileId) =>
      'https://drive.google.com/uc?export=download&id=\$fileId';

  /// Opens folder in Google Drive
  static String folder(String folderId) =>
      'https://drive.google.com/drive/folders/\$folderId';
}

/// MIME Types
class _MimeTypes {
  static const folder = 'application/vnd.google-apps.folder';
  static const spreadsheet = 'application/vnd.google-apps.spreadsheet';

  static const Map<String, String> fileExtensions = {
    'jpg': 'image/jpeg',
    'jpeg': 'image/jpeg',
    'png': 'image/png',
    'gif': 'image/gif',
    'webp': 'image/webp',
    'pdf': 'application/pdf',
    'txt': 'text/plain',
    'doc': 'application/msword',
    'docx':
        'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    'xls': 'application/vnd.ms-excel',
    'xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
  };

  static const fallback = 'application/octet-stream';
}

/// Spreadsheet column headers
class _SheetHeaders {
  static const id = 'ID';
  static const productName = 'Product Name';
  static const price = 'Price';
  static const quantity = 'Quantity';
  static const imageUrl = 'Image URL';

  static List<String> get all => [id, productName, price, quantity, imageUrl];
}

// ============================================================================
// SERVICE CLASSES
// ============================================================================

/// Manages user sessions in Firebase Firestore for single-device enforcement
///
/// This class handles:
/// - Checking if a user can login from a specific device
/// - Creating new session entries in Firestore
/// - Retrieving active device information
/// - Cleaning up sessions on logout
///
/// Firestore Structure:
/// ```
/// user_sessions (collection)
///   └── {email} (document)
///       └── activeSession (map)
///           ├── deviceId: "unique-device-id"
///           ├── deviceName: "Samsung Galaxy S21"
///           ├── loginTime: Timestamp
///           └── lastActive: Timestamp
/// ```
class SessionManager {
  final FirebaseFirestore _firestore = FirebaseFirestore.instance;

  Future<bool> canLogin(String email, String deviceId) async {
    final doc = await _firestore.collection('user_sessions').doc(email).get();

    if (!doc.exists) {
      // No active session, allow login
      return true;
    }

    final activeSession = doc.data()?['activeSession'];
    if (activeSession == null) {
      return true;
    }

    // Check if same device
    if (activeSession['deviceId'] == deviceId) {
      return true; // Same device, allow
    }

    // Different device, session exists
    return false;
  }

  /// Get the name of the device that currently has an active session
  Future<String?> getActiveDeviceName(String email) async {
    final doc = await _firestore.collection('user_sessions').doc(email).get();

    if (!doc.exists) {
      return null;
    }

    final activeSession = doc.data()?['activeSession'];
    if (activeSession == null) {
      return null;
    }

    return activeSession['deviceName'] as String?;
  }

  Future<void> createSession(String email, String deviceId) async {
    await _firestore.collection('user_sessions').doc(email).set({
      'activeSession': {
        'deviceId': deviceId,
        'deviceName': await _getDeviceName(),
        'loginTime': FieldValue.serverTimestamp(),
        'lastActive': FieldValue.serverTimestamp(),
      },
    });
  }

  Future<void> logout(String email) async {
    await _firestore.collection('user_sessions').doc(email).delete();
  }

  Future<String> _getDeviceName() async {
    final deviceInfo = DeviceInfoPlugin();
    if (Platform.isAndroid) {
      final androidInfo = await deviceInfo.androidInfo;
      return '\${androidInfo.brand} \${androidInfo.model}';
    } else if (Platform.isIOS) {
      final iosInfo = await deviceInfo.iosInfo;
      return '\${iosInfo.name} \${iosInfo.model}';
    }
    return 'Unknown Device';
  }
}

/// Get unique device ID
Future<String> _getDeviceId() async {
  final deviceInfo = DeviceInfoPlugin();

  if (Platform.isAndroid) {
    final androidInfo = await deviceInfo.androidInfo;
    return androidInfo.id; // Unique Android ID
  } else if (Platform.isIOS) {
    final iosInfo = await deviceInfo.iosInfo;
    return iosInfo.identifierForVendor ?? 'unknown_ios'; // Unique iOS ID
  }

  return 'unknown_device';
}

/// Structured result of a sign-in attempt
///
/// Instead of throwing exceptions, the handleSignIn method returns this
/// structured result to provide detailed information about the sign-in outcome.
///
/// This enables better error handling and allows the UI to:
/// - Show appropriate messages for different error types
/// - Display device conflict information
/// - Implement waiting/polling mechanisms for device conflicts
///
/// Factory constructors:
/// - `SignInResult.success()` - Successful sign-in
/// - `SignInResult.deviceConflict()` - Another device is logged in
/// - `SignInResult.error()` - Generic error occurred
/// - `SignInResult.cancelled()` - User cancelled the sign-in
class SignInResult {
  final bool success;
  final String? errorMessage;
  final bool isDeviceConflict;
  final String? conflictingDeviceName;
  final String? userEmail;

  SignInResult({
    required this.success,
    this.errorMessage,
    this.isDeviceConflict = false,
    this.conflictingDeviceName,
    this.userEmail,
  });

  factory SignInResult.success() {
    return SignInResult(success: true);
  }

  factory SignInResult.deviceConflict({
    required String deviceName,
    required String email,
  }) {
    return SignInResult(
      success: false,
      isDeviceConflict: true,
      conflictingDeviceName: deviceName,
      userEmail: email,
      errorMessage: 'Account is active on another device',
    );
  }

  factory SignInResult.error(String message) {
    return SignInResult(success: false, errorMessage: message);
  }

  factory SignInResult.cancelled() {
    return SignInResult(
      success: false,
      errorMessage: 'Sign in cancelled by user',
    );
  }
}

/// Main service class for Google Drive & Sheets operations with session management
///
/// This service provides three main areas of functionality:
///
/// **1. AUTHENTICATION & SESSION MANAGEMENT**
///    - Google OAuth 2.0 sign-in/sign-out
///    - Single-device session enforcement via Firebase Firestore
///    - Device conflict detection and resolution
///    - Automatic retry with exponential backoff
///    - Structured error responses (SignInResult)
///
/// **2. GOOGLE DRIVE OPERATIONS**
///    - Upload files to Drive
///    - Create and manage folders
///    - Make files publicly accessible
///    - Generate shareable URLs
///
/// **3. GOOGLE SHEETS OPERATIONS**
///    - Create and manage spreadsheets
///    - Add/read product data
///    - Auto-format headers
///    - Batch operations
///
/// Usage:
/// ```dart
/// final service = GDriveSheetService();
///
/// // Sign in
/// final result = await service.handleSignIn();
///
/// // Upload file
/// final url = await service.uploadFile(file);
///
/// // Add to sheet
/// await service.addProductToSheet(...);
///
/// // Sign out
/// await service.signOut();
/// ```
class GDriveSheetService {
  // Cached current user
  GoogleSignInAccount? _currentUser;

  // Google Sign-In configuration with Drive AND Sheets scopes
  final GoogleSignIn _googleSignIn = GoogleSignIn(
    scopes: <String>[_Scopes.drive, _Scopes.spreadsheets],
    forceCodeForRefreshToken: true,
  );

  /// Get the current authenticated user
  GoogleSignInAccount? get currentUser => _currentUser;

  /// Check if user is authenticated
  bool get isAuthenticated => _currentUser != null;

  /// ========================================================================
  /// AUTHENTICATION METHODS
  /// ========================================================================

  /// Sign in with Google Account
  /// Returns SignInResult with details about the sign-in attempt
  Future<SignInResult> handleSignIn() async {
    try {
      // Step 1: Get device ID
      final deviceId = await _getDeviceId();

      // Step 2: Sign in with Google first (to get email)
      final user = await _googleSignIn.signIn();

      if (user == null) {
        return SignInResult.cancelled();
      }

      // Step 3: Check if can login from this device (with retry)
      final sessionManager = SessionManager();
      final canLogin = await _retryFirestoreOperation(
        () => sessionManager.canLogin(user.email, deviceId),
        operationName: 'canLogin',
      );

      if (!canLogin) {
        // Another device is logged in
        // Get the device name
        final deviceName = await _retryFirestoreOperation(
          () => sessionManager.getActiveDeviceName(user.email),
          operationName: 'getActiveDeviceName',
        );

        // Sign out immediately (don't keep Google signed in)
        await _googleSignIn.signOut();

        // Return device conflict result
        return SignInResult.deviceConflict(
          deviceName: deviceName ?? 'Unknown Device',
          email: user.email,
        );
      }

      // Step 4: Create session (with retry)
      await _retryFirestoreOperation(
        () => sessionManager.createSession(user.email, deviceId),
        operationName: 'createSession',
      );

      // Step 5: Set current user
      _currentUser = user;
      print('✓ Signed in as: \${user.email}');
      print('✓ Session created for device: \$deviceId');

      return SignInResult.success();
    } catch (error) {
      print('✗ Sign in error: \$error');
      return SignInResult.error(error.toString());
    }
  }

  /// Retry Firestore operations with exponential backoff
  ///
  /// Handles transient errors like cloud_firestore/unavailable
  /// Retries up to 3 times with delays: 1s, 2s, 4s
  Future<T> _retryFirestoreOperation<T>(
    Future<T> Function() operation, {
    required String operationName,
    int maxRetries = 3,
  }) async {
    int attempt = 0;
    Duration delay = const Duration(seconds: 1);

    while (true) {
      try {
        attempt++;
        if (attempt > 1) {
          print('⏳ Retry attempt \$attempt for \$operationName...');
        }
        return await operation();
      } catch (e) {
        final isFirestoreUnavailable =
            e.toString().contains('cloud_firestore/unavailable') ||
            e.toString().contains('unavailable') ||
            e.toString().contains('UNAVAILABLE');

        if (isFirestoreUnavailable && attempt < maxRetries) {
          print(
            '⚠️ Firestore unavailable, retrying in \${delay.inSeconds}s... (attempt \$attempt/\$maxRetries)',
          );
          await Future.delayed(delay);
          delay *= 2; // Exponential backoff: 1s -> 2s -> 4s
        } else {
          // Either not a transient error, or max retries reached
          if (isFirestoreUnavailable) {
            print('✗ Firestore still unavailable after \$maxRetries attempts');
          }
          rethrow;
        }
      }
    }
  }

  /// Sign out the current user
  /// Sign out the current user
  Future<void> signOut() async {
    print('🔵 [SERVICE] signOut() called');
    print('🔵 [SERVICE] Current user: \${_currentUser?.email ?? "null"}');

    try {
      // Delete session from Firestore (with retry)
      if (_currentUser != null) {
        print(
          '🔵 [SERVICE] Deleting Firestore session for: \${_currentUser!.email}',
        );
        final sessionManager = SessionManager();
        await _retryFirestoreOperation(
          () => sessionManager.logout(_currentUser!.email),
          operationName: 'logout',
        );
        print('✓ [SERVICE] Session deleted from Firestore');
      } else {
        print('⚠️ [SERVICE] No current user, skipping Firestore cleanup');
      }

      // Sign out from Google
      print('🔵 [SERVICE] Calling Google Sign-In signOut()...');
      await _googleSignIn.signOut();
      print('✓ [SERVICE] Google Sign-In signOut() completed');

      _currentUser = null;
      print('✓ [SERVICE] _currentUser set to null');
      print('✓ [SERVICE] Sign out completed successfully');
    } catch (error) {
      print('✗ [SERVICE] Sign out error: \$error');
      print('✗ [SERVICE] Error type: \${error.runtimeType}');
      rethrow;
    }
  }

  /// Initialize authentication listener
  void initAuthListener(void Function(GoogleSignInAccount?) onUserChanged) {
    _googleSignIn.onCurrentUserChanged.listen(onUserChanged);
    signInSilently();
  }

  /// Attempt silent sign-in
  Future<void> signInSilently() async {
    try {
      final user = await _googleSignIn.signInSilently();
      _currentUser = user;
      if (user != null) {
        print('✓ Silent sign-in successful');
      }
    } catch (error) {
      print('ℹ Silent sign in failed (expected if user never signed in)');
    }
  }

  /// ========================================================================
  /// GOOGLE DRIVE METHODS
  /// ========================================================================

  /// Get MIME type from file extension
  String _getMimeType(String fileName) {
    final ext = fileName.split('.').last.toLowerCase();
    return _MimeTypes.fileExtensions[ext] ?? _MimeTypes.fallback;
  }

  /// Get or create a folder in Google Drive
  Future<String> getOrCreateFolder(String folderName) async {
    if (_currentUser == null) {
      throw Exception('Not authenticated. Please sign in first.');
    }

    try {
      final headers = await _currentUser!.authHeaders;

      // Search for existing folder
      print('🔍 Searching for folder: \$folderName');
      final query =
          'name="\${folderName.replaceAll('"', '\\\\"')}" and mimeType="\${_MimeTypes.folder}" and trashed=false';
      final searchQuery = Uri.parse(_DriveEndpoints.search(query));

      final searchRequest = http.Request('GET', searchQuery)
        ..headers.addAll(headers);

      final searchResponse = await searchRequest.send();
      final searchResponseBody = await searchResponse.stream.bytesToString();

      if (searchResponse.statusCode == 200) {
        final searchJson = jsonDecode(searchResponseBody);
        final files = searchJson['files'] as List?;

        if (files != null && files.isNotEmpty) {
          final folderId = files[0]['id'];
          print('✓ Folder found with ID: \$folderId');
          return folderId;
        }
      }

      // Create new folder
      print('📁 Creating new folder: \$folderName');
      final createUri = Uri.parse(_DriveEndpoints.files());

      final createRequest = http.Request('POST', createUri)
        ..headers.addAll(headers)
        ..headers['Content-Type'] = 'application/json'
        ..body = jsonEncode({
          'name': folderName,
          'mimeType': _MimeTypes.folder,
        });

      final createResponse = await createRequest.send();
      final createResponseBody = await createResponse.stream.bytesToString();

      if (createResponse.statusCode != 200) {
        throw Exception(
          'Failed to create folder: \${createResponse.statusCode}',
        );
      }

      final folderJson = jsonDecode(createResponseBody);
      final folderId = folderJson['id'];

      if (folderId == null) {
        throw Exception('No folder ID returned from Google Drive');
      }

      print('✓ Folder created with ID: \$folderId');
      return folderId;
    } catch (e) {
      print('✗ Folder error: \$e');
      rethrow;
    }
  }

  /// Make file publicly accessible and get Google Drive viewer URL
  ///
  /// Parameters:
  ///   - fileId: Google Drive file ID
  ///
  /// Returns: Google Drive viewer URL (opens file in Drive when clicked)
  ///
  /// What it does:
  /// 1. Adds 'anyone' permission to file (makes it public)
  /// 2. Generates Google Drive viewer URL
  /// 3. Anyone with link can view file in their Drive
  ///
  /// URL Format: https://drive.google.com/file/d/FILE_ID/view?usp=sharing
  /// - Clickable in Google Sheets
  /// - Opens in Google Drive viewer
  /// - Shows file preview
  /// - Allows download from Drive interface
  Future<String> makeFilePublicAndGetUrl(String fileId) async {
    if (_currentUser == null) {
      throw Exception('Not authenticated. Please sign in first.');
    }

    try {
      final headers = await _currentUser!.authHeaders;

      print('🔐 Making file public: \$fileId');
      final permissionUri = Uri.parse(_DriveEndpoints.permissions(fileId));

      final permissionRequest = http.Request('POST', permissionUri)
        ..headers.addAll(headers)
        ..headers['Content-Type'] = 'application/json'
        ..body = jsonEncode({'role': 'reader', 'type': 'anyone'});

      final permissionResponse = await permissionRequest.send();

      if (permissionResponse.statusCode == 200) {
        print('✓ File permissions updated');
      } else {
        print('⚠️ Warning: Failed to update permissions (non-critical)');
      }

      // Return Google Drive viewer URL (opens in Drive when clicked)
      final viewerUrl = _DriveUrls.viewer(fileId);
      print('✓ Drive URL: \$viewerUrl');

      return viewerUrl;
    } catch (e) {
      print('✗ Permission error: \$e');
      rethrow;
    }
  }

  /// Upload file to Google Drive
  Future<String?> uploadFile(
    File file, {
    String folderName = _Defaults.driveFolderName,
  }) async {
    if (_currentUser == null) {
      throw Exception('Not authenticated. Please sign in first.');
    }

    try {
      final headers = await _currentUser!.authHeaders;
      final fileName = file.path.split('/').last;
      final fileBytes = await file.readAsBytes();
      final fileSizeMB = (fileBytes.length / (1024 * 1024)).toStringAsFixed(2);

      print('📤 Uploading: \$fileName (\$fileSizeMB MB)');

      // Get or create folder
      final folderId = await getOrCreateFolder(folderName);

      // Create file metadata
      print('📝 Creating file metadata...');
      final createUri = Uri.parse(_DriveEndpoints.files());

      final createRequest = http.Request('POST', createUri)
        ..headers.addAll(headers)
        ..headers['Content-Type'] = 'application/json'
        ..body = jsonEncode({
          'name': fileName,
          'parents': [folderId],
        });

      final createResponse = await createRequest.send();
      final createResponseBody = await createResponse.stream.bytesToString();

      if (createResponse.statusCode != 200) {
        throw Exception(
          'Failed to create file metadata: \${createResponse.statusCode}',
        );
      }

      final fileJson = jsonDecode(createResponseBody);
      final fileId = fileJson['id'];

      if (fileId == null) {
        throw Exception('No file ID returned from Google Drive');
      }

      print('✓ File metadata created: \$fileId');

      // Upload file content
      print('💾 Uploading file content...');
      final uploadUri = Uri.parse(_DriveEndpoints.fileUpload(fileId));

      final uploadRequest = http.Request('PATCH', uploadUri)
        ..headers.addAll(headers)
        ..headers['Content-Type'] = _getMimeType(fileName)
        ..bodyBytes = fileBytes;

      final uploadResponse = await uploadRequest.send();

      if (uploadResponse.statusCode != 200) {
        throw Exception('Upload failed: \${uploadResponse.statusCode}');
      }

      print('✓ File uploaded successfully');

      // Make file public and get URL
      final publicUrl = await makeFilePublicAndGetUrl(fileId);

      print('✅ Upload complete! URL: \$publicUrl');
      return publicUrl;
    } catch (e) {
      print('✗ Upload error: \$e');
      rethrow;
    }
  }

  /// ========================================================================
  /// GOOGLE SHEETS METHODS
  /// ========================================================================

  /// Get or create a spreadsheet in user's Google Sheets
  ///
  /// Returns: Spreadsheet ID
  Future<String> getOrCreateSpreadsheet(String spreadsheetName) async {
    if (_currentUser == null) {
      throw Exception('Not authenticated. Please sign in first.');
    }

    try {
      final headers = await _currentUser!.authHeaders;

      // Search for existing spreadsheet in Drive
      print('🔍 Searching for spreadsheet: \$spreadsheetName');
      final query =
          'name="\${spreadsheetName.replaceAll('"', '\\\\"')}" and mimeType="\${_MimeTypes.spreadsheet}" and trashed=false';
      final searchQuery = Uri.parse(_DriveEndpoints.search(query));

      final searchRequest = http.Request('GET', searchQuery)
        ..headers.addAll(headers);

      final searchResponse = await searchRequest.send();
      final searchResponseBody = await searchResponse.stream.bytesToString();

      if (searchResponse.statusCode == 200) {
        final searchJson = jsonDecode(searchResponseBody);
        final files = searchJson['files'] as List?;

        if (files != null && files.isNotEmpty) {
          final spreadsheetId = files[0]['id'];
          print('✓ Spreadsheet found with ID: \$spreadsheetId');
          return spreadsheetId;
        }
      }

      // Create new spreadsheet
      print('📊 Creating new spreadsheet: \$spreadsheetName');
      final createUri = Uri.parse(_SheetsEndpoints.create());

      final createRequest = http.Request('POST', createUri)
        ..headers.addAll(headers)
        ..headers['Content-Type'] = 'application/json'
        ..body = jsonEncode({
          'properties': {'title': spreadsheetName},
          'sheets': [
            {
              'properties': {
                'title': _Defaults.sheetName,
                'gridProperties': {
                  'frozenRowCount': 1, // Freeze header row
                },
              },
            },
          ],
        });

      final createResponse = await createRequest.send();
      final createResponseBody = await createResponse.stream.bytesToString();

      if (createResponse.statusCode != 200) {
        throw Exception(
          'Failed to create spreadsheet: \${createResponse.statusCode}\\n\$createResponseBody',
        );
      }

      final spreadsheetJson = jsonDecode(createResponseBody);
      final spreadsheetId = spreadsheetJson['spreadsheetId'];

      if (spreadsheetId == null) {
        throw Exception('No spreadsheet ID returned');
      }

      print('✓ Spreadsheet created with ID: \$spreadsheetId');

      // Add headers to the spreadsheet
      await _addHeadersToSheet(spreadsheetId, headers);

      return spreadsheetId;
    } catch (e) {
      print('✗ Spreadsheet error: \$e');
      rethrow;
    }
  }

  /// Add headers to the spreadsheet
  Future<void> _addHeadersToSheet(
    String spreadsheetId,
    Map<String, String> authHeaders,
  ) async {
    try {
      print('📝 Adding headers to spreadsheet...');

      final range = '\${_Defaults.sheetName}!A1:E1?valueInputOption=RAW';
      final updateUri = Uri.parse(
        _SheetsEndpoints.values(spreadsheetId, range),
      );

      final updateRequest = http.Request('PUT', updateUri)
        ..headers.addAll(authHeaders)
        ..headers['Content-Type'] = 'application/json'
        ..body = jsonEncode({
          'values': [_SheetHeaders.all],
        });

      final updateResponse = await updateRequest.send();
      final updateResponseBody = await updateResponse.stream.bytesToString();

      if (updateResponse.statusCode == 200) {
        print('✓ Headers added successfully');

        // Format headers (bold)
        await _formatHeaders(spreadsheetId, authHeaders);
      } else {
        print(
          '⚠️ Warning: Failed to add headers: \${updateResponse.statusCode}\\n\$updateResponseBody',
        );
      }
    } catch (e) {
      print('⚠️ Warning: Error adding headers: \$e');
    }
  }

  /// Format headers (make them bold)
  Future<void> _formatHeaders(
    String spreadsheetId,
    Map<String, String> authHeaders,
  ) async {
    try {
      final formatUri = Uri.parse(_SheetsEndpoints.batchUpdate(spreadsheetId));

      final formatRequest = http.Request('POST', formatUri)
        ..headers.addAll(authHeaders)
        ..headers['Content-Type'] = 'application/json'
        ..body = jsonEncode({
          'requests': [
            {
              'repeatCell': {
                'range': {'sheetId': 0, 'startRowIndex': 0, 'endRowIndex': 1},
                'cell': {
                  'userEnteredFormat': {
                    'textFormat': {'bold': true},
                  },
                },
                'fields': 'userEnteredFormat.textFormat.bold',
              },
            },
          ],
        });

      final formatResponse = await formatRequest.send();

      if (formatResponse.statusCode == 200) {
        print('✓ Headers formatted (bold)');
      }
    } catch (e) {
      print('⚠️ Warning: Error formatting headers: \$e');
    }
  }

  /// Add a product row to the spreadsheet
  ///
  /// Parameters:
  ///   - id: Unique ID (use UUID)
  ///   - productName: Name of the product
  ///   - price: Price of the product
  ///   - quantity: Quantity
  ///   - imageUrl: URL from Google Drive upload
  Future<bool> addProductToSheet({
    required String id,
    required String productName,
    required String price,
    required String quantity,
    required String imageUrl,
    String spreadsheetName = _Defaults.spreadsheetName,
  }) async {
    if (_currentUser == null) {
      throw Exception('Not authenticated. Please sign in first.');
    }

    try {
      final headers = await _currentUser!.authHeaders;

      // Get or create spreadsheet
      final spreadsheetId = await getOrCreateSpreadsheet(spreadsheetName);

      print('📝 Adding product to sheet...');

      final range = '\${_Defaults.sheetName}!A:E';
      final appendUri = Uri.parse(
        _SheetsEndpoints.append(spreadsheetId, range),
      );

      final appendRequest = http.Request('POST', appendUri)
        ..headers.addAll(headers)
        ..headers['Content-Type'] = 'application/json'
        ..body = jsonEncode({
          'values': [
            [id, productName, price, quantity, imageUrl],
          ],
        });

      final appendResponse = await appendRequest.send();
      final appendResponseBody = await appendResponse.stream.bytesToString();

      if (appendResponse.statusCode == 200) {
        print('✓ Product added to sheet successfully');
        return true;
      } else {
        print(
          '✗ Failed to add product: \${appendResponse.statusCode}\\n\$appendResponseBody',
        );
        return false;
      }
    } catch (e) {
      print('✗ Error adding product to sheet: \$e');
      return false;
    }
  }

  /// Get all products from the spreadsheet
  Future<List<Map<String, dynamic>>> getAllProducts({
    String spreadsheetName = _Defaults.spreadsheetName,
  }) async {
    if (_currentUser == null) {
      throw Exception('Not authenticated. Please sign in first.');
    }

    try {
      final headers = await _currentUser!.authHeaders;

      // Get spreadsheet ID
      final spreadsheetId = await getOrCreateSpreadsheet(spreadsheetName);

      print('📖 Reading products from sheet...');

      final range = '\${_Defaults.sheetName}!A2:E';
      final readUri = Uri.parse(_SheetsEndpoints.values(spreadsheetId, range));

      final readRequest = http.Request('GET', readUri)..headers.addAll(headers);

      final readResponse = await readRequest.send();
      final readResponseBody = await readResponse.stream.bytesToString();

      if (readResponse.statusCode == 200) {
        final responseJson = jsonDecode(readResponseBody);
        final values = responseJson['values'] as List?;

        if (values == null || values.isEmpty) {
          print('ℹ No products found');
          return [];
        }

        final products = values.map((row) {
          return {
            'id': row.length > 0 ? row[0] : '',
            'productName': row.length > 1 ? row[1] : '',
            'price': row.length > 2 ? row[2] : '',
            'quantity': row.length > 3 ? row[3] : '',
            'imageUrl': row.length > 4 ? row[4] : '',
          };
        }).toList();

        print('✓ Found \${products.length} products');
        return products;
      } else {
        print('✗ Failed to read products: \${readResponse.statusCode}');
        return [];
      }
    } catch (e) {
      print('✗ Error reading products: \$e');
      return [];
    }
  }
}

```
