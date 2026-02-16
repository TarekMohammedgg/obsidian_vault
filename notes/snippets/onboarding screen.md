

```dart 

import 'package:stock_application/common.dart';


class OnBoardingScreen extends StatelessWidget {
  const OnBoardingScreen({super.key});
  static String id = 'OnBoardingScreen';
  @override
  Widget build(BuildContext context) {
    final controller = Get.put(OnBoardingController()) ;
    return Scaffold(
      body: Stack(
        children: [
          PageView(
            controller: controller.pageController,
            onPageChanged: controller.updatePageIndicator,
            children: [
              OnBoardingPage(
                image: kSearchingImagePath,
                title: "Welcome to Stock App",
                subTitle:
                    "Your gateway to smarter investing and real-time market insights",
              ),
              OnBoardingPage(
                image: kShoppingImagePath,
                title: "Welcome to Stock App",
                subTitle:
                    "Your gateway to smarter investing and real-time market insights",
              ),
              OnBoardingPage(
                image: kMemoryStorageImagePath,
                title: "Welcome to Stock App",
                subTitle:
                    "Your gateway to smarter investing and real-time market insights",
              ),
              OnBoardingPage(
                image: kCariousImagePath,
                title: "Welcome to Stock App",
                subTitle:
                "Your gateway to smarter investing and real-time market insights",
              ),
            ],
          ),
          const OnBoardingSkip(),
          const OnBoardingNavigation(),
          const OnBoardingNextButton()
        ],
      ),
    );
  }
}
```