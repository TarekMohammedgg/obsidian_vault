#flutter #flutter_basics
مثال علي ال final و ال late : 

```dart
// final Example : 
class Student {
final String name ; 
Student (String name ){this.name = name }
}
// in main 
student1 = Student("yourName")
student1.name = "changename" ;  // this code Not Run
```

----
```dart
// late Example : 
class Student {
late String name ; 
Student(){
this.name = "userName" ; 
}
}
```
