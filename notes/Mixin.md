#software #oop 
عبارة عن حل بديل لل multiple [[Inheritance]] من خلال انك  بتعمل extract لـ Behavior معين من ال classes من الي  كنت  عايز تعملهم inherit علي جنب كده لوحده . 

```dart 
// Example 
mixin CanWak{
wak(){
print("can waking"); 
}
}
mixin CanTalk{
talk(){
print("can talking");
}
}
abstract class Robot {
final String name
Robot(this.name) ; 
}
class WakingRobot extends Robot with CanWak{
WalkingRobot(super.name); 

} 
class TalkingRobot extends Robot with CanTalk{
TalkingRobot(super.name); 

}
class AiRobot extends Robot with CanTalk , CanWalk{
AiRobot(super.name); 
}
void main () {

}
```

اقدر اعمل override علي ال mixin methods 