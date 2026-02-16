
#flutter #flutter_architecture 
related : [[how flutter framework build]] 

---
=> Flutter : A declarative , multi-platform UI framework written in Dart , heavily supported by Google . 


*declarative:* mean that is like React and SwiftUI , and can sync and rebuild the code depend on the status . 

*multi-platform:* can run on  Windows ,Linux , Mac OS , Android and Web . 


the language used for Flutter Framework is Dart (created in 2013) , Dart prop is single thread loop like JavaScript 


=>  Flutter framework have custom class name [[widgets]]


=> state full hot reload => in 2018 . 


=> there are three tree structure for flutter framework :
1- Widget Tree 

2- Element Tree 
- provide imperative implementation 
- long-lived object 
- like glue code with widget and render layers 

3- Render Tree 


=> any flutter project contain three important component : 
1- native project like HTML in web or xcode in ios 
2- Dart source code 
3- some platform specific glue code to launch all the dart code together . 

=> flutter use in render things `Skia` (graphic engine that used in google chrome , android and many  other products )  in the past , but know use `Impeller` 


=>*Flutter layered cake :* 
1- Framework Dart 
2- Engine c/c++ : the engine that handle graphics and communication with operating system throw embedders 
3- platform-specific embedders 

