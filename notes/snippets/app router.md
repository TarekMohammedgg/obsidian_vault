

```dart
import 'package:bookly/features/home/presentation/views/book_details.dart';
import 'package:bookly/features/home/presentation/views/home_view.dart';
import 'package:bookly/features/search/presentation/views/search_view.dart';
import 'package:bookly/features/splash/presentation/views/splash_view.dart';
import 'package:go_router/go_router.dart';

abstract class AppRouter {
  static const khomeView = '/homeView';
  static const kbookDetailsView = '/bookDetailsViews';
  static const ksearchView = '/searchView';
  static final router = GoRouter(
    routes: [
      GoRoute(
        path: '/',
        builder: (context, state) => const SplashView(),
      ),
      GoRoute(
        path: khomeView,
        builder: (context, state) => const HomeView(),
      ),
      GoRoute(
        path: kbookDetailsView,
        builder: (context, state) => const BookDetailsViews(),
      ),
      GoRoute(
        path: ksearchView,
        builder: (context, state) => const SearchView(),
      ),
    ],
  );
}

```