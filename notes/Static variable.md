#flutter #flutter_basics
- معني اني هيبقي عندي variable ليه  reference ثابت في الـ memory يعني مثلا لو عايز اعمل مثال ال increment counter عندي دخول طالب جديد هخلي ال counter variable يبقي Static variable عشان يبقي ليه reference ثابت في كل مره اجي ازود القيمة ازودها في نفس ال reference و بما إني قولت انه هيكون ليه reference واحد يبقي مينفعش انادي عليه غير من ال class نفسه مش من ال object 
- و ال static بيبقي تابع لل class مش لل object 

```dart 
class Student {
  static int counter = 0;
  final String name;
  Student(this.name) {
    counter++; }
}

void main() {

  Student student1 = Student("name_1");

  Student student2 = Student("name_2");

  print(Student.counter); // will be 2 
}
```

