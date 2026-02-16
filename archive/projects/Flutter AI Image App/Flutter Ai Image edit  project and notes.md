---
due_date: 2025-10-27
tags:
  - Flutter/project
  - Main
status: complete
parent:
Area:
start_date: 2025-11-01
end_date: 2025-11-30
---
- used this design from `dribble` website: [UI Design](https://dribbble.com/shots/25438640-Pico-Smart-AI-Photo-Editor-Mobile-App-Design)

>[!note]- how to install `Firebase` on your app ? 
>- we need in the first check if you are logged in or not by: `firebase login` 
>- second `dart pub global activate flutterfire_cli`
>- third `flutterfire configure` to choose your project or create a new project

>[!note]- what is `Firebase Logic Ai` ? 
>- is a feature in `firebae console` make the users can use the ai models directly and with very easy method on our applications 
>- there are two types of plans : 
>	1. `gemini ` have free tier 
>	2. `vertix` (paid plan)
>- `gemini-flash-image` => not available for free 
>-  `gemini-falsh` => available and awesome, using `firebase logic Ai` found in `firebase console` 


`image.memory()` => take the bytes image
`image.file()` => take the file format of the image 

>[!note]- how to support markdown in flutter ? 
>- using the package names: `flutter_markdown` 
>- it has two option 
>- `Markdown` : that support scrollable features and more advanced features 
>- `MarkdownBody` : support `Markdown` without scrollable feature 

>[!note]- how to add feature animate the text like `...` until response on the request ? 
>using the package : `animated_text_kit`
>```dart
> if (message.text.startsWith("Thinking")) {
return AnimatedTextKit(
  repeatForever: true,
  isRepeatingAnimation: true,
  animatedTexts: [TyperAnimatedText("...")],
);
>```

>[!note]- supported models in `gemini` plan in `firebase logic ai` ? 
>https://firebase.google.com/docs/ai-logic/models

### when using .mp() with async - await  operation that cause some problem because the task end before wait the future event done so the best practice is use for or future.forEach() like the next example 
	### ```dart 
	import 'dart:io';
	import 'package:firebase_ai/firebase_ai.dart';
	
	abstract class GoogleAiService {
	  static Future<String> generateText(
	    String? notes,
	    List<String?> imagesPath,
	  ) async {
	    final model = FirebaseAI.googleAI().generativeModel(
	      model: "gemini-2.5-flash",
	    );
	
	    final text = "Answer this question briefly and clearly: ${notes ?? ''}";
	    final textPart = TextPart(text);
	
	    final List<Part> imagesPart = [];
	
	    // ✅ Properly await each image read
	    for (final path in imagesPath) {
	      if (path == null) continue;
	      final file = File(path);
	      if (!file.existsSync()) continue;
	
	      final bytes = await file.readAsBytes();
	      imagesPart.add(InlineDataPart("image/jpeg", bytes));
	    }
	
	    // ✅ Merge parts safely
	    final List<Part> parts = [
	      textPart,
	      if (imagesPart.isNotEmpty) ...imagesPart,
	    ];
	
	    final prompt = Content.multi(parts);
	
	    // ✅ Generate response
	    final response = await model.generateContent([prompt]);
	    final result = response.text?.trim() ?? "try again";
	
	    return result;
	  }
	}
	
	```



### if you want to make the background of top item in the stack of the navigators transparent use the next 
  ```dart 
  onPressed: () {

              Navigator.of(context).push(

                PageRouteBuilder(

                  opaque: false,

                  pageBuilder: (_, __, ___) =>

                      const GalleryOverlayWithCaption(),

                ),

              );

            },
  ```

>[!note]- how to when send close the keyboard automatically ? 
>```dart 
>FocuseScope.of(context).unfocuse; 
>``` 


>[!note]- how to save image to gallery ? 
>gallery_saver and its forked packages (like image_gallery_saver) are outdated.
>the stackoverflow link : https://stackoverflow.com/questions/49987707/how-to-save-an-image-to-the-photo-gallery-using-flutter
>don't forget the next `AndroidManifest.xml` file : 
>```dart 
><uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
>```


>[!note]-  what is the different between `File` and `XFile` and `Unit8List` ? 
>`File` => `dart:io `represent the device filesystem 
>`XFile` => found in `Image_picker` is custom , wee need to convert to `File` to can process it 
>`Unit8List` =>`dart:typed_data` represent the raw byte format , used when send the image over network 

### think about add the in-app purchase feature . 

### `InteractiveViewrWidget` => to can manipulate the child , like zoom or rotate . 

>[!note]- what is the diff between `Map` and `.Entries`  ? 
>`Map` direct   return the map key and value and we should convert the map key and value to `MapEntry()` that used when i want to convert from map to another map (the mean of convert is if you want to edit on the already map and save it like add 10 points or add some value to the current value in the map ) 
>
>`Entries` mean when to get the `Iterable` item to use it for present that on the screen like `Widgets`  

### Expanded works with Column or Row or Flex 
- قابلتني مشكلة اثناء عمل ال filters الا و هي اني كنت عايز اعمل download للصورة بعد تطبيق filter عليها ، و عشان احل المشكلة دي استخدمت widget في فلاتر اسمها `RepaindRendr` و فيه برده package اسمها `Screenshot` بتعمل نفس المهمة. 

### to make a slider bar use the next code 
```dart 
	double value = 50;

Slider(
  value: value,
  min: 0,
  max: 100,
  divisions: 100,
  label: value.round().toString(),
  onChanged: (newValue) {
    setState(() {
      value = newValue;
    });
  },
)

	```
or ... 
```dart 
RotatedBox(
  quarterTurns: 3,
  child: Slider(
    value: value,
    min: 0,
    max: 100,
    onChanged: (newValue) {
      setState(() {
        value = newValue;
      });
    },
  ),
)

```

### how to apply blur filter in the image ? 
take care the ``BackdropFilter`` widget not effect on the parent widget 

### open the camera just when the app is opened 
- we can do it using the `camera` package in flutter . 
```dart 
Future<void> initCamera() async {
    final cameras = await availableCameras();
    controller = CameraController(cameras.first, ResolutionPreset.medium);
    await controller!.initialize();
    setState(() => isReady = true);
  }
```
- don't forget add the next dependencies in `android/app/build.gradle`
  ```dart 
  dependencies {


    // Fix for missing class file
    implementation("androidx.concurrent:concurrent-futures:1.1.0")

    // Force stable CameraX versions (avoid 1.5.0-beta)
    implementation("androidx.camera:camera-core:1.3.4")
    implementation("androidx.camera:camera-camera2:1.3.4")
    implementation("androidx.camera:camera-lifecycle:1.3.4")
    implementation("androidx.camera:camera-view:1.3.4")
    implementation("androidx.camera:camera-extensions:1.3.4")
}
  ```


- can't make the `initstate` be async the same thing in `setstate((){})`
- `ClipRRect` widget check the blur doesn't exceed the limit of the image in blur process 

---
### to display the recent images from the photo 
use the `photo manager` package that allow you get the stream of bytes that make the image and get the all type of media like (audio , video , images) like the stream the same thing we do to connect with `gemini` when call `then((){})` method to get the return message from `gemini` 
```dart 
 List<AssetEntity> images = [];

  Future<void> fetchAssets() async {
    images = await PhotoManager.getAssetListRange(
      start: 0,
      end: 20,
      type: RequestType.image,
    );
    setState(() {});
  }
```
this code will return `20` images (just images ) from the photo gallery 

#### what is the diff between `getAssetListRange({start, end})` and `getAssetListPaged({page, size})` ? 
Difference:
`getAssetListRange({start, end})`
Returns a fixed range of assets by index.
Example: start: 0, end: 20 → gets the first 20 assets.
Not optimized for pagination or lazy loading.
Useful for a small, static subset.
`getAssetListPaged({page, size})`
Returns assets in pages for better performance and infinite scrolling.
Example: page: 0, size: 50 → first 50 assets, then page: 1 for the next 50.
Preferred for displaying image galleries.
✅ Use getAssetListPaged for production (scrolling gallery).
✅ Use getAssetListRange only for quick fetches or testing.

ميزة ال `future builder ` انها جزئية ال future انها بتستني متعرضش ال builder غير ما ال snapshot يبدأ يجي 

