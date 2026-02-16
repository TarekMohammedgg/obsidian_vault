
```dart

import 'package:stock_application/common.dart';

class OnBoardingNextButton extends StatelessWidget {
  const OnBoardingNextButton({
    super.key,
  });

  @override
  Widget build(BuildContext context) {
    return Positioned(
        right: 27,
        bottom: 20,
        child: ElevatedButton(
            onPressed: () => OnBoardingController.instance.nextPage() ,
            style: ElevatedButton.styleFrom(
              shape: const CircleBorder(),
              padding: const EdgeInsets.all(12), // Increases overall button size
              backgroundColor: kMySecondaryColor,



            ),
            child: const Icon(
              Icons.arrow_forward_ios_sharp,
              size: 25,
              color: Colors.black,
            )));
  }
}
```