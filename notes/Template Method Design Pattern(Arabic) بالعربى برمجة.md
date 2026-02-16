---
title: "Template Method Design Pattern(Arabic) بالعربى #برمجة"
source: https://www.youtube.com/watch?v=r1MOYIyMWyQ
author:
  - "[[DevGeeks Academy]]"
published: 2021-10-12
created: 2025-12-01
description: Design Patterns بالعربىالكودhttps://gist.github.com/Mostafico/d82d8b153a830a406496c3463fb5e70dDesign Patterns قائمة تشغيلhttps://www.youtube.com/watch?v=-UQN...
tags:
  - Software/Design-Pattern
  -  
image: https://img.youtube.com/vi/r1MOYIyMWyQ/maxresdefault.jpg
date: 2025-12-01
---
فكرة ال design pattern هي انك توفر Template جاهز (فيه مجموعة من الخطوات الشبه ثابته و المشتركه ما بين اكتر من class ) بدل ما اكررها لا اخدها بره كـ template و يكون abstract ، و اعمل abstract method للجزئية الي بتميز ال class الي واخدين inherite من ال template abstract class . 

زي مثال البيتزا خطوات عمل البيتزا ثابته و لكن فيه بعض الخطوات الي ممكن تتغير زي مثلا شكل البيتزا عايزها circle or rectangl ؟ فهنا احنا بنعمل abstract template class فيه خطوات عمل البيتزا و بعدين اعمل two class بيورثوا من ال template class و بيعملوا override علي ال shape method بتاعة ال pizza و بكده ابقي وفرت كود و خليته scalable . 


فيه بعض ال pitfalls الا و هي اني كده خليت ال interitance classes تمشي علي خطوات شبه ثابته و محدده  . 

