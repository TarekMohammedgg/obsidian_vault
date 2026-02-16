---
date: 2025-11-30
tags:
  - Software/Design-Pattern
  -  
---
ايه هو ؟؟ و امتي بنحتاجه ؟؟ 
مثال العامل الذكي و الاقل ذكاء لما تيجي تسأله علي ال Action اي المفروض يعمله علي ال current state الي معاه بيقعد يعمل check من خلال if - else كثيره عشان يشوف ال action الي المفروض يعمله ، اما العامل الذكي بيجيب كل state و بيفتحها و يبقي كاتب ال state الفلاني و ال action 

امتي تحتاجها ؟؟ 
لما يكون عندي اكتر من state محتاجين اعملهم handle() 
بيطبق مبدأ [[Solid Principles MOC]] خاصة ال [[O - Open Close Principle]] بحيث عملت extension لل state بس مجتش جمب ال worker . 
