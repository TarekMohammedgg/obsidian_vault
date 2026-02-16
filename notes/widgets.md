#flutter #flutter_architecture 
- provide declarative api 
- immutable , disposable

is custom classes in flutter have all important rendering and have two things (optional constructor and build method )



Widgets have essential Method named build method and have an essential parameter name `BuildContext`
for having the runtime values like the screen size and the orientation , Accessibility info and text direction 


the build method must in the end return a single widget . 


----
=> *the 3 main widgets flavors:*

```dart
abstract class Widget{}

abstract class SatelessWidget extends Widget {}
// display one aspect from UI 

abstract class StatefulWidget extends Widget {}
// the build method wrapped with State Object managed by  second tree structure (element Tree)

abstract class RenderObjectWidget extends Widget {} 

abstract class InheritedWidget extends Widget {} 
// not render date by it self , but it pass it 
```