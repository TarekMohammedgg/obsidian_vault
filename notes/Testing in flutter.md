---
due_date:
  - - 2025-10-10
tags:
  - testing
related: "[[flutter]]"
share_link: https://share.note.sx/r5kwo4ji#geBpbavb0UVnckKKjwyVCj+sS/AvQMC/rm6uxo25lc0
share_updated: 2025-10-11T16:34:43+03:00
---
# Unit Testing 
## Mock Dependency in flutter 
اولا كلمة "mock" معناها شيء وهمي او مش حقيقي . 
في الوضع الطبيعي لما اجي عايز اعمل testing لـ Function بتحتاج انها تستدعي حاجة من الباك او من حاجه خارجية انا كمطور تطبيقات مليش يد فيها او مقدرش اتحكم فيها فده هيخل من الاختبار و هيخليه مش مظبوط ، فالحل في الموقف ده اني اعمل زي server او باك وهمي بحيث يكون ليا التحكم الكامل في جميع اجزاء ال testing عشان اضمن ان الجزء بقي بتاعي اني انا عامله في حد ذاته شغال فعلاً ، يعني الفكرة ببساطه انا عايز اختبر الفانكشن بتاعتي  و اتأكد اني بختبرها هيا فعلا مش حاجه تانيه عن طريق اني بعمل حاجه وهمية و بفترضها انها شغاله و تمام . 

### Setup 
install packages `Mockito` dependencies and `build_runner` in dev dependencies 
create a new folder named mocks in test folder for mocks include the class you want to mock up it 
```dart 
import 'package:dio/dio.dart';

import 'package:mockito/annotations.dart';

  

@GenerateNiceMocks([MockSpec<Dio>()])

import 'dio_mock_test.mocks.dart';
```
then run builder runner => `flutter pub run build_runner build` 
then use the created file  in your testing file 

---

[[what is the diff between sync and async star and await and parallel operations ]]

### what is the diff between `thenAnswer` and `theReturn` ? 

`then answer ` => used when return future 

`thenReturn` => when return value not come in the future 



# Widget Testing 
عندنا في ال test widget  هي عبارة عن بيئة عمل Environment عشان تعملي render لل widget الي عايز اعملها Test 

```dart 
// testWidgets() -> like test() (responsible for creating an environment)
// but take in the callback parameter tester from type WidgetTester 
//WidgetTester: is the helper or the controller and responsible for rendering your widget that you want to test it 
// 💡Take care : testWidget callback is Future , because rendering the widget in WidgetTester take sometime 
```
## what is `testWidget()` do in real ? 
1. create fake flutter app environment (no emulator , no phone) , create widget tree 
2. give you a `WidgetTester` 
3. It uses something called **`TestWidgetsFlutterBinding`** — a special class that:
	- Controls the **rendering**, **timing**, and **input** in tests.
	- Makes sure animations, timers, and rebuilds are controlled (so your test doesn’t hang or depend on real time).
4. isolate each test 
5. Flutter’s `testWidgets()` also handles `await` automatically.
6. 