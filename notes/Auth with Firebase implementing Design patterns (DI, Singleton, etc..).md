1- Add dependencies to `pubspec.yaml`:

```dart
dependencies:
  flutter:
    sdk: flutter
  firebase_core: ^3.0.0
  firebase_auth: ^5.0.0
  flutter_riverpod: ^2.5.0
  shared_preferences: ^2.2.3
```

2- Initialize Firebase in your app:

- Add `google-services.json` (Android) and `GoogleService-Info.plist` (iOS).
- In `main.dart`:

```dart
void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  runApp(ProviderScope(child: MyApp()));
}
```

---

## Clean Architecture Layers

We’ll split into:

- **Data layer** → talks to Firebase & SharedPreferences
- **Domain layer** → contains repository interface & entities
- **Application layer** → providers (Riverpod)
- **Presentation layer** → UI widgets & pages

---

## Data Layer

**AuthService (Firebase API wrapper)**

```dart
import 'package:firebase_auth/firebase_auth.dart';

class AuthService {
  final FirebaseAuth auth;
  AuthService(this.auth); // DI

  Future<User?> login(String email, String password) async {
    final result = await auth.signInWithEmailAndPassword(
      email: email,
      password: password,
    );
    return result.user;
  }

  Future<User?> register(String email, String password) async {
    final result = await auth.createUserWithEmailAndPassword(
      email: email,
      password: password,
    );
    return result.user;
  }

  Future<void> logout() async {
    await auth.signOut();
  }

  User? get currentUser => auth.currentUser;
}

```

---

### LocalStorageService (SharedPreferences)

```dart
import 'package:shared_preferences/shared_preferences.dart';

class LocalStorageService {
  final SharedPreferences prefs;
  LocalStorageService(this.prefs); //DI

  Future<void> saveToken(String token) async {
    await prefs.setString("auth_token", token);
  }

  String? getToken() {
    return prefs.getString("auth_token");
  }

  Future<void> clearToken() async {
    await prefs.remove("auth_token");
  }
}
```

---

## Domain Layer

### AuthRepository (abstraction)

```dart
import 'package:firebase_auth/firebase_auth.dart';

abstract class AuthRepository {
  Future<User?> login(String email, String password);
  Future<User?> register(String email, String password);
  Future<void> logout();
  User? getCurrentUser();
}
```

---

### AuthRepositoryImpl (implementation)

```dart
import 'package:firebase_auth/firebase_auth.dart';
import 'auth_repository.dart';
import '../services/auth_service.dart';
import '../services/local_storage_service.dart';

class AuthRepositoryImpl implements AuthRepository {
  final AuthService authService;
  final LocalStorageService localStorage;

  AuthRepositoryImpl(this.authService, this.localStorage);

  @override
  Future<User?> login(String email, String password) async {
    final user = await authService.login(email, password);
    if (user != null) {
      await localStorage.saveToken(user.uid); // save uid as token
    }
    return user;
  }

  @override
  Future<User?> register(String email, String password) async {
    final user = await authService.register(email, password);
    if (user != null) {
      await localStorage.saveToken(user.uid);
    }
    return user;
  }

  @override
  Future<void> logout() async {
    await authService.logout();
    await localStorage.clearToken();
  }

  @override
  User? getCurrentUser() => authService.currentUser;
}

```

---

## **Application Layer (Riverpod Providers)**

```dart
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:shared_preferences/shared_preferences.dart';
import '../data/services/auth_service.dart';
import '../data/services/local_storage_service.dart';
import '../data/repositories/auth_repository_impl.dart';
import '../domain/auth_repository.dart';

// FirebaseAuth provider
final firebaseAuthProvider = Provider<FirebaseAuth>((ref) {
  return FirebaseAuth.instance;
});

// SharedPreferences provider
final sharedPrefsProvider = Provider<SharedPreferences>((ref) {
  throw UnimplementedError(); // initialized later in main
});

// AuthService provider
final authServiceProvider = Provider<AuthService>((ref) {
  final auth = ref.watch(firebaseAuthProvider);
  return AuthService(auth);
});

// LocalStorageService provider
final localStorageProvider = Provider<LocalStorageService>((ref) {
  final prefs = ref.watch(sharedPrefsProvider);
  return LocalStorageService(prefs);
});

// AuthRepository provider
final authRepositoryProvider = Provider<AuthRepository>((ref) {
  final authService = ref.watch(authServiceProvider);
  final storage = ref.watch(localStorageProvider);
  return AuthRepositoryImpl(authService, storage);
});

// AuthNotifier (state management)
class AuthNotifier extends StateNotifier<User?> {
  final AuthRepository repository;

  AuthNotifier(this.repository) : super(repository.getCurrentUser());

  Future<void> login(String email, String password) async {
    final user = await repository.login(email, password);
    state = user;
  }

  Future<void> register(String email, String password) async {
    final user = await repository.register(email, password);
    state = user;
  }

  Future<void> logout() async {
    await repository.logout();
    state = null;
  }
}

final authProvider =
    StateNotifierProvider<AuthNotifier, User?>((ref) {
  final repo = ref.watch(authRepositoryProvider);
  return AuthNotifier(repo);
});

```

---

## Presentation Layer (UI Example)

```dart
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../application/auth_provider.dart';

class LoginPage extends ConsumerWidget {
  final emailController = TextEditingController();
  final passwordController = TextEditingController();

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final user = ref.watch(authProvider);

    return Scaffold(
      appBar: AppBar(title: Text("Login")),
      body: user != null
          ? Center(child: Text("Welcome ${user.email}"))
          : Padding(
              padding: const EdgeInsets.all(16),
              child: Column(
                children: [
                  TextField(controller: emailController, decoration: InputDecoration(labelText: "Email")),
                  TextField(controller: passwordController, decoration: InputDecoration(labelText: "Password")),
                  SizedBox(height: 20),
                  ElevatedButton(
                    onPressed: () {
                      ref.read(authProvider.notifier).login(
                            emailController.text,
                            passwordController.text,
                          );
                    },
                    child: Text("Login"),
                  )
                ],
              ),
            ),
    );
  }
}

```

---

## Main.dart (inject SharedPreferences)

```dart
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'application/providers.dart';
import 'presentation/login_page.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  final prefs = await SharedPreferences.getInstance();

  runApp(
    ProviderScope(
      overrides: [
        sharedPrefsProvider.overrideWithValue(prefs),
      ],
      child: MyApp(),
    ),
  );
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Auth App',
      home: LoginPage(),
    );
  }
}

```

---

### SharedPreferences in Flutter

`SharedPreferences.getInstance()` under the hood is already a **Singleton**.

- It ensures only **one instance** of `SharedPreferences` exists in the whole app.
- So even if you call `SharedPreferences.getInstance()` many times, you always get the same instance.

That means you **don’t need to write your own singleton** for it — Flutter’s package already does that for you