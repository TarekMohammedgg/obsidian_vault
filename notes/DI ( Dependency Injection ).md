**Dependency Injection** = Giving an object the things it needs, instead of letting it create them itself.

**DI** = don’t create dependencies inside → inject them from outside.

- Constructor injection
- Riverpod providers
- Service locators (like get_it)

---

# What DI gives you ?

### 1. **Separation of concerns**

Instead of UI knowing about Firebase, UI only knows about a **repository**

UI → UserRepository → AuthService → FirebaseAuth

If Firebase changes → only `AuthService` changes. UI & repository remain the same

### 2. **Testability**

### 3. Flexibilty for the future

---

**Without DI (tight coupling)**

```dart
class AuthService {
  final FirebaseAuth _auth = FirebaseAuth.instance; // created inside

  Future<User?> login(String email, String password) async {
    final result = await _auth.signInWithEmailAndPassword(
      email: email, 
      password: password,
    );
    return result.user;
  }
}

```

Tight coupling :

- **UI is tied to Firebase**
- If tomorrow i want to switch to **Supabase, REST API, or my own backend**, i’d have to **rewrite every single place** i used `FirebaseAuth`.
- Testing becomes **impossible** (i can’t mock `FirebaseAuth.instance`).

**With DI (loose coupling):**

```dart
class AuthService {
  final FirebaseAuth _auth; // dependency is passed in

  AuthService(this._auth);

  Future<User?> login(String email, String password) async {
    final result = await _auth.signInWithEmailAndPassword(
      email: email, 
      password: password,
    );
    return result.user;
  }
}

```

Loose coupling:

- inject **FirebaseAuth.instance** in production.
- Or inject a **FakeAuth** class in tests.
- `AuthService` doesn’t care _where_ `_auth` comes from ⇒ it only cares that it gets something that behaves like FirebaseAuth

---

# Constructor Injection

```dart
class UserRepository {
  final AuthService authService;

  UserRepository(this.authService); // injected here
}
```

```dart
final repo = UserRepository(AuthService(FirebaseAuth.instance));

```

---

# Riverpod Injection

**Provider** in Riverpod is a **box** that holds your dependency

just `ref.read()` or `ref.watch()` it wherever needed.

```dart
final firebaseAuthProvider = Provider<FirebaseAuth>((ref) {
  return FirebaseAuth.instance;
});
```

Whenever someone needs FirebaseAuth, get it from this provider

```dart
class AuthService {
  final FirebaseAuth auth;
  AuthService(this.auth);

  Future<void> login(String email, String password) async {
    await auth.signInWithEmailAndPassword(email: email, password: password);
  }
}

// Make AuthService a provider
final authServiceProvider = Provider<AuthService>((ref) {
  final auth = ref.watch(firebaseAuthProvider); // inject FirebaseAuth here
  return AuthService(auth);
});

```

didn’t create `AuthService` manually Riverpod is injecting it

Now i have created an `AuthService` class that wraps around `FirebaseAuth`.

Instead of using `FirebaseAuth` directly everywhere in my app, I inject it into `AuthService` through a provider.

The provider (`authServiceProvider`) gives me an instance of `AuthService` with the `FirebaseAuth` it needs.

This way, if I ever want to change the authentication backend (e.g., Supabase instead of Firebase), I only need to update the provider, not every place in the code where authentication is used

usage in UI:

```dart
class LoginButton extends ConsumerWidget {
  const LoginButton({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    return ElevatedButton(
      onPressed: () async {
        final authService = ref.read(authServiceProvider);
        await authService.login("test@test.com", "123456"); // cleaner
      },
      child: Text("Login"),
    );
  }
}
```