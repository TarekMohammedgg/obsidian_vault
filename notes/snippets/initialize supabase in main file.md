
```dart 
void main() async {
  WidgetsFlutterBinding.ensureInitialized();

  await Supabase.initialize(
    url: Consts.kSUPABASE_URL,
    anonKey: Consts.kSUPABASE_ANON_KEY,
  );

  runApp(MyApp());
}
```