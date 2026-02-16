

```dart 
import 'dart:developer';

import 'package:firebase_messaging/firebase_messaging.dart';
import 'package:push_notification_tutorial/main.dart';

class FirebaseApi {
  //create an instance of Firebase Messaging
  final _firebaseMessaging = FirebaseMessaging.instance;
  // function to initialize notifications
  Future<void> initNotifications() async {
    // request premission from user (will prompt user)
    await _firebaseMessaging.requestPermission();
    // fetch the FCM (firebasae cloud  Message) token for this device
    final fCMToken = await _firebaseMessaging.getToken();
    // print the token (normally you would send this to your server)
    log("Token: \$fCMToken");
    //initialize further settings for push notification
    initPushNotifications();
  }

  // function to handle recieved messages
  void handelMessage(RemoteMessage? message) {
    // if the message is null , nothing
    if (message == null) return;

    // navigate to new screen when message is recieved and user taps notification

    navigatorKey.currentState?.pushNamed(
      "/notification_screen",
      arguments: message,
    );
  }

  // function to initialize foreground and background settings
  Future<void> initPushNotifications() async {
    // handle notification if the app was terminated and new opened
    FirebaseMessaging.instance.getInitialMessage().then(handelMessage);

    // attach event listeners for when a notification open the app
    FirebaseMessaging.onMessageOpenedApp.listen(handelMessage);
  }
}

```