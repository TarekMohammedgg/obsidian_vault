

```dart
import 'package:stock_application/common.dart';
class OnBoardingNavigation extends StatelessWidget {
  const OnBoardingNavigation({
    super.key,
  });

  @override
  Widget build(BuildContext context) {
    final controller = Get.put(OnBoardingController());
    return Positioned(
        left: 27,
        bottom: 40,
        child: SmoothPageIndicator(
          effect: const ExpandingDotsEffect(
              activeDotColor: kMySecondaryColor, dotHeight: 10),
          controller:controller.pageController,
          onDotClicked: controller.dotNavigationClick,
          count: 4,
        ));
  }
}

```