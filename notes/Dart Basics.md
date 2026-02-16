### Overview 
- اي لغة برمجة بيقي فيها / ليها Start Point يعني نقطة تبدأ من عندها و الي في لغة ال Dart هيبقي اسمها main و دي عبارة عن function 
```dart 
void main () {

}
```

- في Dart بعد اي سطر برمجة تحط (;) 
### comment 
- ال comments حاجه مهمة في ال flutter خاصة  لما تعمل حاجة اسمها [[widgets]] عشان تعرف كل widget بتعمل ايه 
```dart 
// -> single comment 
/*multiple comment*/  
```

### Variable 
- Data types :  float , integers , double , bool , String , List (Array) 
- ممكن نعبر عن اي متغير بكلمة 'var' 
> [!INFO] print the value 
```dart
String name = "Your Name" ; 
print(name) ; 
// OR 
print("your name is :$name" ) ; 
```

> [!INFO] String Literals & Interpolation 
> التعامل مع النصوص 
- Scape Character => "`\` " `BackSlash`
- Interpolation : 
سطر علي بعضه فيه ال String + value 
- لو عايز تعمل عمليات علي المتغير ده زي انك تعرف ال length بتاعه قد ايه ازاي نعمل كده ؟ 
```dart 
print("your length of the name : ${name.length}) ; 
```

> [!INFO] the Diff between var and constant and final 
> - const : must be known at compile time , and can't be changed . locate in the memory 
> - final : must be known at runtime  , and can't be changed . 

### Control Flow 
```dart 
if () {}
else if () {}
else {}
```

> [!INFO] Condition Expression 
> case 1 : `condition ? Accepted : Rejected ; `
> case 2 (give default value):
> 
> 
```dart 
String name = null ; 
String user = name ?? "Guest" ; 
print("hello, ${user}") ; 
// the expected return is "Guest" 
```  

>[!INFO] Switch Cases
>اكنك عايز تعمل Rules في ال Code 

### FOR LOOP 
1) For LOOP 
```dart 
List names = ["First" , "Second"] ; 
// Basic for loop 
for (String name in names ){
print(name) ; 
}
// using ForEach loop 
names.forEach((name){print($name)}) ; 
// بس خلي بالك الطريقة دي بتنفع مع ال  
// Lists 
```
2) While LOOP
3) Do while LOOP 
4) Break and Continue 
> [!INFO] Named for loop 
>
```dart 
OuterLoop: for(){} 
```

-----
### Functions 
> [!INFO] Arrow Function 
```dart 
Void printName (String name) => print("your name is : $name");
```

> [!INFO] Optional Parameter 
```dart 
void Names (String firstName , [String? lastName 2 ])
```
خلي بالك لازم تعمل حساب ال NULL Safety فلازم تخلي ال string يبقي Nullable علي مسؤوليتك الخاصة . 


> [!INFO] Named Parameters 
```dart 
int calculate_xyz ({int x , int y , int z}){
return x*y*z ; 
}
void main () {
// when using this function : 
result = calculate_xyz(x:1 , y:2 , z:3) ; 
print(result) ; 
// return 6 
}
```

> [!INFO] Default Function (Give the parameter default value)
```dart 
int calculate (int x  , int y = 1 ){
return x * y ; 
}
// if the y value not given from the user the default value is 1 
```

>Lambda Expression 
```dart 
Function x = (int y , int z) {return y+z ; }
Function x = (int y , int z ) => x+y ; 
```

---- 
[[Null Safety]]

----
### Error Handling 
الهدف منه لو عايز handling مشكلة داخل ال Application ، يعني في ال Runtime باستخدام : 
```dart 
try {} 
catch (){}
finally{} // (optional) must done if try or catch done 
// if you know the error name replace 'catch ()' with 'on ErrorName'
```

-----
[[Archive/MOCS 1/OOP MOC]]

> [!INFO] Callable Function 
> معناها اني اتعامل مع ال class اكنه Function و اعمل call للحاجات الي جوه ال class  و ده بيتم من خلال  
```dart 
class SayHello {
  String call(String name) {
    return "Your name is: $name";
  }
}

void main() {
  var hello = SayHello();
  print(hello("Tarek"));
}
```

---
### Extra Dart 

- Dart Fixed list : 
```dart 
List <data type> = List(size) ; 
```
- Growable List : 
```dart 
List<int> human = [] ; 
var listName = List<data type>.filled(size , initial value) ; 
//listName.add() ; 
//listName.remove(value) ;
//listName.removeAt(index) 
```



- Dart Set 
نفس نظام ال List و لكن من غير تكرار 
```dart 
void main() {
List<int> numbers = [1,2,3,4,5,6,6,7] ; 
Set setNumbers = Set.from(numbers) ; 
print(setNumbers) ; 
//print(setNumbers.contains(4)) ; return true  
}
```

- Dart Map 
```dart 
void main() {
Map mapName = {"tarek" : 1 , "Mohammed" : 2 , "yahya" : 3 } ; 
print(mapName.keys) ; // return (tarek, Mohammed, yahya)
print(mapName.values) ; // return (1, 2, 3)
}
```
