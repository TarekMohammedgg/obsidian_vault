# sync متزامن 
معناها ان العمليات بتحصل بترتيب منطقي خطوه خطوه 
```dart 
print("A");
print("B");
print("C");
//Answer
//A
//B
//C
```
# async غير متزامن 
بيبقي شكل الداتا الي جايالي `Future` يعني مش هستلمها في الوقت الحالي ، هستلمها في المستقبل . 
يعني بيبقي فيه حاجة شغاله في ال Background ، و البرنامج يكمل شغله عادي في نفس الوقت. 
```dart
print("A");
Future.delayed(Duration(seconds: 2), () => print("B"));
print("C");
```

```dart
A
C
B
```

# async *  
بيستخدم مع ال Stream يعني الداتا الي جايالي عبارة عن `Stream` 
```dart
// async
Future<int> getNumber() async {
  return 5;
}

// async*
Stream<int> getNumbers() async* {
  yield 1;
  yield 2;
  yield 3;
}

```

# await 
هنا انت بتقول استني العملية دي تخلص قبل ما تكمل الكود الي بعده 
```dart
Future<void> getData() async {
  print("Getting data...");
  await Future.delayed(Duration(seconds: 2));
  print("Data ready!");
}
```

```dart 
void main() async {
  print("Start");
  await getData(); // هنا بيستنى
  print("End");
}
```

```dart 
Start
Getting data...
Data ready!
End
```

# parallel operations 
هنا العمليتين بيشتغلوا مع بعض في نفس الوقت بشكل تبادلي بحيث لما الاولي بتنتظر حاجة تحصل من الباك اند بدل ما اقعد استناها و خلاص لأ ، بروح علي التاسك التانيه اخلص فيها برده حاجات لحد ما يجيلي الرد من الاولي . 







