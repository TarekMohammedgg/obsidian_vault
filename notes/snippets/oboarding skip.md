
```dart
import 'package:stock_application/common.dart';
class OnBoardingSkip extends StatelessWidget {
  const OnBoardingSkip({
    super.key,
  });

  @override
  Widget build(BuildContext context) {
    return Positioned(
        top: 50,
        left: 280,
        child: TextButton(
            onPressed: () => OnBoardingController.instance.skipPage() ,
                // Navigator.pushReplacementNamed(context, LoginPage.id),
            child: const Text(
              "Skip",
              style: TextStyle(color: kMySecondaryColor, fontSize: 14),
            )));
  }
}


```