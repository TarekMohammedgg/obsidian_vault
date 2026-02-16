#software #oop 

inheritance : [[Inheritance]] 
في ال inheritance بتكون العلاقة ما بين ال child و ال parent 
child **is a** parent
عشان انت بتاخد كل الصفات الي عند ال parent بالاضافه الي الصفات الخاصة بالـ child  . 

---

composition : 
لما تكون العلاقة ما بين ال class و الـ class التاني هي 
class 1 has a class 2 
يبقي ساعتها يفضل استخدام composition 

طب  ازاي استخدمه ؟ 
```dart 
// Example 
class Monitor {
display (){
print("displaying monitor") ; 
}
}
class Keyboard {
display(){
print("the keyboard is typing"); 
}
} 
// computer has a monitor and keyboard
class Computer {
Monitor monitor = Monitor() ; 
Keyboard keyboard = Keyboard() ; 
display(){
print("computer is Starting"); 
monitor.display(); 
keyboard.display(); 
}
}

// main 
void main (){
Computer computer1 = Computer(); 
computer.display() ; 
}
```

