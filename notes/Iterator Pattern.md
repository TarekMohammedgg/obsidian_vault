[[Design Pattern]]
#source/Youtube #status/inProgress 

----
### يعني ايه ؟ 

هو عبارة عن اكنك جبت Protocol او شباك موحد بتتعامل بيه مع ال data types المختلفة ، بحيث اكنك جبت سكرتارية هو المسؤولة عن جلب البيانات بتاعتك و انت ك client ملكش علاقة بال implementation الي بيحصل . 

فيه انواع من ال Iterators عندي 


immutable  iterators 
بيبقي عنده next and has next ، و لكن لو انت عايز تتحكم اكتر و تعرف برده الي قبل كده او تعرف مثلا ال index بتاع ال value الي انت فيها ساعتها بتروح لـ 
mutable iterators 
بيبقي عنده مميزات اكتر زي index , previous and has previous 


### العيوب 
بيبقي ابطأ شوية عن ما استخدم ال for loop العادية بتاعتي او اني اعملها انا بشكل Manually .  