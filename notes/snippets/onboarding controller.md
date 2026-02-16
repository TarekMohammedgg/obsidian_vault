
```dart

import 'package:stock_application/common.dart';


class  OnBoardingController extends GetxController {
  static OnBoardingController get instance => Get.find() ;
  //varialbes
  final pageController = PageController() ;
  Rx<int> pageCurrentIndex = 0.obs ;
  //Methods
  void updatePageIndicator (index) => pageCurrentIndex.value= index ;
  void dotNavigationClick(index) {
    pageCurrentIndex.value = index ;
    pageController.jumpToPage(index) ;
  }
  void nextPage() {
    if(pageCurrentIndex.value == 3 ) {
      Get.to(() =>  LoginPage() )  ;
    }else {
      int   page = pageCurrentIndex.value + 1 ;
      pageController.jumpToPage(page) ;
    }
   }
  // void previousPage() {
  //   int page = pageCurrentIndex.value - 1 ;
  //   pageController.jumpToPage(page) ;
  // }
  void skipPage(){
    pageCurrentIndex.value = 3 ;
    Get.offAll(() =>LoginPage()) ;
  }
}
```