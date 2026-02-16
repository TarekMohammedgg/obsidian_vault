---
due_date: 2025-10-06
tags:
  - flutter
  - flutter_notifications
related: "[[flutter]]"
---
notification like a reminder for user to do action or inform him anything . 
### types of notifications 
there are many types of notifications but the main common used in flutter are 
Push notifications 
Local notifications 

----
## Push Notification
like the what's app chat the notification come from outside app like when the user like your video notify the user , this thing like [[Observer Design Pattern]] 
### Setup 
we need before start install `flutterfire cli` 
then login to firebase 
```bash
firebase login
```
then activate `flutterfire cli`
```bash
dart global activate flutterfire_cli
```
to see your projects on firebase use  : 
```bash 
firebase projects:list 
```
then configure the flutter fire to choose the project your want to link you firebase with it 
```bash 
flutterfire configure 
```
after linking your app with firebase , you need to install important packages 
```bash 
flutter pub add firebase_core
```
```bash 
flutter pub add firebase_messaging
```
then ensure you initialize  the firebase before start the app 
```dart
void main() async {

  WidgetsFlutterBinding.ensureInitialized();

  await Firebase.initializeApp(options: DefaultFirebaseOptions.currentPlatform);

  runApp(const MyApp());

}
```
then start create the api code to initialize the notification and receive it and take action 
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

    // fetch the FCM (firebasae cloud  Message) token for this device

    final fCMToken = await _firebaseMessaging.getToken();

    // print the token (normally you would send this to your server)

    log("Token: $fCMToken");

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
----
## Local Notifications 
mean the notification come from flutter it self in specific time the user determine it or developer determine it (like after 7 days if the user didn't open the app then notify him ) 

### Setup 
first, we need to install package `flutter_local_notifications`
```bash 
flutter pub add flutter_local_notifications
```
then 
follow the steps in this [[Flutter Local Notifications]]



