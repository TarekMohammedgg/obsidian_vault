#software #SOLID_principles 
related:: [[Archive/MOCS 1/flutter]]
- Coupling  
	- high / tightly coupling : الاتنين بيعتمدوا علي بعض 
	- Loose coupling : اعتماد اقل و ده الهدف 

----
[[S - Single Responsibility Principle]]
[[O - Open Close Principle]]
[[L - Liskov Substitution Principle]]
[[I - Interface Segregation Principle]]
[[D - Dependency Inversion Principle]]

-----

SOLID principles are **five core design principles** in object-oriented programming (OOP) that help us write **clean, maintainable, and scalable code**. They were introduced by Robert C. Martin (Uncle Bob).

- **S** → One job per class.
- **O** → Add new stuff without breaking old.
- **L** → Subclasses should behave like parent.
- **I** → Smaller, specific interfaces.
- **D** → Depend on abstractions, not implementations.

---

## **S — Single Responsibility Principle (SRP)**

A class should have **only one reason to change**.

Each class should focus on doing **one thing** well.

Right:

```dart
class UserRepository {
  Future<User> getUserFromApi() {...}
}

class UserCache {
  void saveUser(User user) {...}
  User? getUser() {...}
}
```

one class only **fetches users**, the other only **caches users**

Wrong:

```dart
class UserManager {
  Future<User> getUserFromApi() {...}
  void saveUser(User user) {...}
  User? getUser() {...}
}
```

This class does **too many things** (fetch + cache)

---

## **O — Open/Closed Principle (OCP)**

Classes should be **open for extension**, but **closed for modification**. Instead of modifying existing code, extend it with new functionality.

Right:

```dart
abstract class Payment {
  void pay(double amount);
}

class PayPalPayment implements Payment {
  @override
  void pay(double amount) => print("Paid $amount with PayPal");
}

class StripePayment implements Payment {
  @override
  void pay(double amount) => print("Paid $amount with Stripe");
}
```

Now if i add ApplePay, i just create a new class.

I don’t **modify** existing ones.

Wrong:

```dart
class Payment {
  void pay(String method, double amount) {
    if (method == "paypal") ...
    else if (method == "stripe") ...
  }
}
```

Here, adding a new method means modifying the class.

---

## **L — Liskov Substitution Principle (LSP)**

Subtypes should be replaceable with their base type **without breaking the code**.

Right:

```dart
abstract class Bird {
  void fly();
}

class Sparrow extends Bird {
  @override
  void fly() => print("Flying...");
}
```

Sparrow can replace Bird without issues.

Wrong:

```dart
class Bird {
  void fly() {}
}

class Ostrich extends Bird {
  @override
  void fly() {
    throw Exception("Ostriches can't fly!");
  }
}
```

If we replace Bird with Ostrich, code breaks. Violation of LSP.

---

## I — Interface Segregation Principle (ISP)

No client should be forced to depend on methods it does not use.

Break large interfaces into smaller, more specific ones.

Right:

```dart
abstract class Printer {
  void printDocument();
}

abstract class Scanner {
  void scanDocument();
}

class MultiFunctionPrinter implements Printer, Scanner {
  @override
  void printDocument() {...}

  @override
  void scanDocument() {...}
}
```

Wrong:

```dart
abstract class Machine {
  void printDocument();
  void scanDocument();
}

class SimplePrinter implements Machine {
  @override
  void printDocument() {...}

  @override
  void scanDocument() {
    throw Exception("This printer can't scan");
  }
}
```

SimplePrinter is forced to implement `scanDocument` it doesn’t need.

---

## D — Dependency Inversion Principle (DIP)

High-level modules should not depend on low-level modules.

Both should depend on **abstractions**.

Right::

```dart
abstract class AuthService {
  Future<void> login();
}

class FirebaseAuthService implements AuthService {
  @override
  Future<void> login() async => print("Login with Firebase");
}

class AuthController {
  final AuthService service;
  AuthController(this.service);

  void authenticate() => service.login();
}
```

Now AuthController can use **any service** (Firebase, Supabase, etc.), just by injecting it.

Wrong:

```dart
class AuthController {
  final FirebaseAuthService service = FirebaseAuthService();
  void authenticate() => service.login();
}
```

Here, AuthController is **tightly coupled** with Firebase. Hard to replace.