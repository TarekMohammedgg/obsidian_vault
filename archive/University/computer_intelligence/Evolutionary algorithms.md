هو العلم المتخص في دراسة الظواهر الطبيعية و محاكاتها في صورة algorithms 



### Types of Evolutionary Algorithms 


- un informed search  (exhaustive search) or (Brute force ) :
يعني بتعدي علي كل ال States الموجوده عندك في ال search space كلها بطريقة معينه .. فالموضوع بيبقي مرهق  .

انواعه : 
1- Depth First search (Back Search) 
2- Breadth First Search

- informed search (Heuristic search ): 
ببدأ بقي اطلع معلومات من ال states الي بعدي عليها و مش شرط اعدي علي ال Search pace كلها 
و لكن في مقابل ده هو مش بيضمنلك انه يوصلك لاحسن حل ممكن في ال Search space عشان الموضوع ده بيعتمد علي ال Heuristic information الي انت جمعتها و انت ماشي في ال Search space . 

انواعه : 
1- Greedy Search 
2- Best First Search 

مميزاتها : 
1- انها بتحاول علي قد ما تقدر انها متقعش في ال local optima
2- ممكن تتعامل مع district values (categorical ) زي ("A" , "B") . 

types of heuristic algos ? 
1- Swarm intelligence : 
ببساطه بيبقي ذكاء طالع من مجموعات (افراد)
و من اشهر ال Algorithms الي من النوع ده . 
[[computer_intelligence - lecture 02 -  Ant colony (ACO)]]

practical Swarm 

2- [[computer intelligence - lecture 01 - Simulating Annealing]] 

3- genetic Algorithm . 

و خلي بالك كل ال heuristic algos الي اتكلمنا عليها دي فيها جزء من ال Randomness شوية برده بالاضافه الي ال 
heuristic Gaudiness rules  
