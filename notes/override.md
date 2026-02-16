- معناها انك عايز تعدل علي Function موجوده بالفعل ، مع اضافة زيادات من عندك 
```dart 
void eat (){
super.eat() ; 
print("_") ; 
}
```

### inheritance with constructor 
```dart 
class Human {
int age ; 
}
Class Student extends Human {
Student(): super(){}
}
```

- what is the meaning of initialize class ? 
	- معناها اني اقدر اعمل منه Object 
	- و الكلام ده مش موجود في ال [[Abstraction]] ، لان الهدف من ال Abstraction هو الوراثة منه فقط وليس عمل Object منه . 
- 