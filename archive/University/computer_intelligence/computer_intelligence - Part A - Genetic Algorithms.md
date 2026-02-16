
what is [[Evolutionary algorithms]]

[[Types of Ai Agents]]

### Genetic Algorithms (population based Algorithm)
الي بيخلي ال GA افضل من ال Classical search algos ، هو : 
1- ان ال GA ممكن يتعامل مع complicated search space . 
2- عندك في ال Classical search algos ممكن تقع بسهوله في  local optimal  بسهوله لانها بتشتغل علي ايجاد حل واحد بس باستخدام لاما gradient descent or gradient ascent ، علي عكس ال GA انها بتوجد اكتر من حل و بتقارن ما بينهم كلها فاحتما ان الحل بتعها يكون Global optimal بيبقي اكبر بكتير من ال Classical search algorithms ، و خلي بالك كمان ال solution دي بيتم ايجادها علي التوازاي  يعني بنستخدم اكتر من Climber في نفس الوقت و كل واحد فيهم بيلاقي حل  و بناخد احسن حل فيهم . 

ال Algorithm بيعتمد علي two concepts : 
1- Natural selection 
بكل بساطه البقاء للاصلح / الاقوي the fittest survive 
2- Genetic inheritance 
توريث الصفات الي traits للاجيال الجاية ، و ممكن يبقي فيه صفات مش ظاهره او بتظهر في ظروف او شروط معينه . 
و يبقي فيه genes قوية (dominant) و تانيه (recessive) 

فالبتالي احنا بنحاكي نظام الطبيعة اثناء حل المشكلة ، يعني مثلا في الطبيعة (problem) بيبقي الافراد الي عايشين فيها سواء بقي حيوانات او بشر (solution) الي بيقدر يتعايش مع الطبيعة و يتقالم هو الي بيسود / هو الي بيفضل عايش يعني فهو ده المبدأ الي عايزين نطبقه . 


offspring : الجيل الجديد 

عندنا في ال Genetic algorithms بيركز اكتر علي ال Recombination اكتر من ال mutation ، فيه بعض ال Algorithms في عائلة ال [[Evolutionary algorithms]] بتبقي مركزه اكتر علي ال [[mutation]] زي ال [[computer_intelligence - Differential Evolution]] 

و بيبقي ال termination مش ثابت ، يعني ممكن يبقي انك تقول انا هوقفه لما يبقي عدد ال offspring  يبقي 100 مثلا ، او لما اوصلل solution نسبة ال error بتاعته او ال accuracy عند رقم معين ، اول لما يبقي التغير ما بين الجديد و الي قبله حاجات بسيطه يعني مفيش فرق كبير . 

implementation of GA : 
1-stochastic operators : 
- [[selection in EA]] 
- [[recombination - crossover]] 
- [[mutation]] 

2- steps 
1:- [[representation of the solution problems in EA]] 
2:- build fitness function == Heuristics
بتبدأ تحطط بقي ايه هي المشكلة او المعايير بحيث تبقي زي مرشد ليك يقولك حل كده الحل ده كويس ولا لأ . 
مثال : عندنا في example ال 8 queens 
فكرة الحل انك عايز كل queen تبقي في مكان متقدرش تهاجم بيه queen تانية و ال queen التانية متقدرش تهاجمها برده ، و الموضوع ده مش هيحصل الا لما يكون ال queen محدش موجود معاه علي نفس العمود او الصف او حتي بشكل قطري ، ففي الحالة دي بيكون ال fitness function بتاعتنا هنا اننا بنشوف شكل ال environment الي عندنا و نشوف  كل كوين تقدر تهاجم كام queen تانيه يعني لو تقدر تهاجم 3 يبقي نحسبها معانا و بعدين نشوف queen تانيه و نشوف هي تقدر تهاجم كام queens نقول مثلا 2 يبقي كده المجموع عندي هيبقي 5 و ده بنسميه ال penalty الي هو مقدار كسر القاعده او الخطأ ففي الحالة دي كلما كان كبير كان شيء وحس و المفروض الهدف اننا نحسنه ، طبعا انا اقدر اتحكم في الكيفية يعني مثلا ممكن اجيب ال inverse يعني penalty / 1 و ده هيبقي fitness فكلما زاد كان شيء كويس و كلما قل كان شيء وحش.
3:- select parents for recombination  : 
ببدأ اختار parents عشان اعملهم cross over و بيتم اختيارهم علي اساس fitness function ، يعني ممكن اقول مثلا اني هختار بشكل عشوائي خمسه مثلا و بعدين اشوف احسن اتنين من الخمسه دول علي اساس ال fitness function عشان يكونوا parents و بعدين اعمل recombination ، و اكرر الكلام ده تاني يعني اجيب  5 جداد تاني بشكل عشوائي و بعدين اعمل Selection عشان انتج two children تانين و ممكن يكون فيه تكرار في ال parents ممكن يحصل لو ال parent ده ال fitness بتاعته عاليه .
مثال توضيحي :


و طريقة ال selection دي اسمها tournament selection ، و في كل مره بنختار 5 جداد 

4:- Mutation (Exploration): 


5:- replacement 
و فيه اكتر من طريقة عشان اقدر اعمل replacement ، من ضمن الطرق دي حاجه اسمها  
Elitism 
بمعني انك بتخلي احسن 5% مثلا من ال  parents من الجيل القديم يبقوا لسه موجودين في الجيل الجديد و الباقي يبقي نتاج من ال offspring 

بعض الملحوظات ممكن تعمل اكتر من selection في نفس ال generation  و لكن بشرط  ان عدد ال children يكون قد او اقل من عدد ال population و عملية ال selection تبقي علي نفس ال population الي انت باديء بيه ، و بعد ما توصل لعدد ال children الي انت محدده تبقي تعمل mutation لو عايز و بعدين تعمل Replacement ، بالطريقة بقي المناسبة 
