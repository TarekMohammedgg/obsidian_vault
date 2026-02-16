

```dart 
import 'dart:developer';

import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:gdrive_tutorial/consts.dart';
import 'package:gdrive_tutorial/gapi_constatns.dart';
import 'package:gdrive_tutorial/session_manager.dart';
import 'package:gdrive_tutorial/shared_prefs.dart';
import 'package:google_sign_in/google_sign_in.dart';

class AuthClient {
  AuthClient() {
    init();
  }
  GoogleSignIn gSignIn = GoogleSignIn.instance;
  bool isInitialid = false;
  late GoogleSignInAccount? _currentUser;
  late GoogleSignInClientAuthorization? _auth;
  GoogleSignInAccount? get currentUser => _currentUser;
  SessionManager sessionManager = SessionManager();

  set currentUser(newCurrentUser) {
    _currentUser = newCurrentUser;
  }

  GoogleSignInClientAuthorization? get auth => _auth;
  set auth(newAuth) {
    _auth = newAuth;
  }

  Future<GoogleSignInAccount?> attemptSilentSignIn() async {
    await ensureIntialid();

    try {
      // ✅ Attempt silent authentication (v7.2.0)
      final account = await gSignIn.attemptLightweightAuthentication();
      _auth = await gSignIn.authorizationClient.authorizeScopes(
        GoogleApiConstants.scopes,
      );
      if (account != null) {
        log('✅ Silent sign-in successful: ${account.email}');
        _currentUser = account;
        return account;
      } else {
        log('⚠️ No cached credentials available');
        return null;
      }
    } catch (error) {
      log('❌ Silent sign-in failed: $error');
      return null;
    }
  }

  Future<void> init() async {
    // ServerClientID is the ClientID for web Oauth in google console api
    try {
      await gSignIn.initialize(
        serverClientId: GoogleApiConstants.serverClientId,
      );
      isInitialid = true;
    } catch (e) {
      log("Failed to initialied");
    }
  }

  Future<void> ensureIntialid() async {
    if (!isInitialid) {
      await init();
    }
  }

  Future<void> login() async {
    await ensureIntialid();
    if (!gSignIn.supportsAuthenticate()) {
      log("Google Sign-in not Ready");
    }

    try {
      currentUser = await gSignIn.authenticate(
        scopeHint: GoogleApiConstants.scopes,
      );
      if (currentUser != null) {
        await CacheHelper.saveData("Email", currentUser!.email);
        final photoUrl = currentUser!.photoUrl;
        if (photoUrl != null && photoUrl.isNotEmpty) {
          await CacheHelper.saveData("ProfileImage", photoUrl);
          log("Profile Image URL: $photoUrl");
        }
      }
      auth = await gSignIn.authorizationClient.authorizeScopes(
        GoogleApiConstants.scopes,
      );
      if (auth != null) {
        await CacheHelper.saveData("AccessToken", auth!.accessToken);
      }
      try {
        final currentDevice = await sessionManager.getDeviceName();
        final sessionDoc = await FirebaseFirestore.instance
            .collection(kFirebaseStoreCollectionName)
            .doc(currentUser!.email)
            .get();
        if (sessionDoc.exists) {
          final activeSession = sessionDoc
              .data()?[kFirebaseStoreActiveSessions];
          final deviceName = activeSession?[kDeviceInfoName];
          if (currentDevice != deviceName) {
            sessionManager.addToFireStore();
          }
        }
        sessionManager.addToFireStore();
      } catch (e) {
        log("Error when create session");
      }
    } catch (e) {
      log('Google Sign-In Error: $e');
    }
  }

  Future<void> logout() async {
    try {
      await gSignIn.signOut();
      currentUser = null;
    } catch (e) {
      log("Error in Sign out: ${e.toString()}");
    }
  }
}

```