

```dart
routes: {
              HomeScreen.id: (context) => HomeScreen(),
              LoginPage.id: (context) => LoginPage(),
              RegisterPage.id: (context) => RegisterPage(),
              OnBoardingScreen.id: (context) => const OnBoardingScreen(),
              ScanQrCode.id: (context) => HomeScreen(),
              Welcome.id: (context) => const Welcome(),
              AddProduct.id: (context) => AddProduct(),
              ProductScreen.id: (context) => const ProductScreen(),
              AuthCheck.id: (context) => AuthCheck() ,
              ImageUploadCompressPage.id : (context) => ImageUploadCompressPage() ,
              ImageUpload.id : (context) => ImageUpload() ,
            },
            initialRoute: ImageUploadCompressPage.id,
```