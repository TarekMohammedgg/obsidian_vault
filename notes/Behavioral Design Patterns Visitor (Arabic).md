---
date: 2025-12-09T15:15:55+02:00
tags:
  - 
  - Software/Design-Pattern
image: https://i.ytimg.com/vi/UqWBlht131g/maxresdefault.jpg
source:
  - https://www.youtube.com/watch?v=UqWBlht131g&list=PLd-dOEgzBpGnt3GuEszo_piQq52XSqAmj&index=12&t=22s
---

فكرة ال design pattern دي هي اني عايز اطبق tax او اعمل calculate لاكتر من class or object و كل object بيبقي ليه حسبه مختلفه عن غيره ، فالبتالي الحل انك تكتب طريقة ال calculate دي داخل كل class or object و لكن الطريقة دي غير عمليه او غير مجزية لانها ممكن يبقي فيها اخطاء كتيره ده كمان انها مش بتطبق مبدأ ال  [[O - Open Close Principle]] لذلك الحل هو اني اجيب وسيط اسمه Visitor بيتم توكيله من قبل ال main class و هو بقي بيعمل visit لكل ال objects بقي الي عايز احسب عندها ال calculate المعينه دي ، و لكن قبل ما يقدر يعمل Visit ليهم لازم يكون Accept Visit من طرف ال Main class and other objects اكني عملتله verify . 

PitFalls : 
- من احد اضرار ال Design ده هو لو حبينا نزود ال Scale بتاعنا هنضطر نعدل في ال visitor و نعدل في ال visit verificatons و نعدل في ال Main object ، فهنضطر اننا نعدل في اكتر من مكان 
- تاني عيب هو ان ال visitor ممكن يبقي عايز يعرف private attributes عن ال other objects عشان يقدر يعمل Calculate بتاعته دي .. فده هنيخليه يعرف معلومات خاصة و ده برده افضل حاجه . 
