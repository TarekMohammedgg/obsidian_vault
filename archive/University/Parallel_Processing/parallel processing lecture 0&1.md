---
---

----
### Definition of parallel processing ? 
هي عبارة عن  طريقة في ال computing (عمليات الخاصة بالكمبيوتر ) ، بحيث هي **عبارة عن اي عملية يتم فيها تقسيم task الي subtasks علي اتنين**  ، سواء اتنين processors (CPUs) او اكتر ، او حتي لو كان multi-core processors  المهم يكون فيه تاسك اتقسم ل subtasks اتوزعت علي اكتر من object سواء كان CPU or core    ، و ده بيزود ال performance بتاع ال system الي شغال عليه . 

لو جينا لنقطة مين الاحسن ال multi-core or multi-processors هيبقي الافضل ال multi-core عشان ده هيوفر في استهلاك الجهاز للطاقة بالاضافة الي انه ممكن يكون ارخص . 

### how parallel processing improve the performance of system ? 
من خلال انه بيسرع عملية ال computational و كمان بيقلل ال throughput ( عدد الاوامر الي الجهاز بيخلصها في الثانية الواحده )   

### parallel processing classification  ?
#### pre-requirement before know what is parallel classification ?   
normal operation of computer is fetch instruction and fetch that in memory 
**instruction stream** 
sequence of instruction that reads from memory  

**data stream**
some of operations that performs on data 

\- parallel processing can perform on one of two classification or both . 
#### parallel classification
1. SISD : single instruction - single data (single processor )
2. SIMD : single instruction - multiple data 
3. MISD : multiple instructions - single data 
4. MIMD : multiple instructions - multiple data 

#### SISD 
single processor may or may not apply parallel processing  (pipelining processing or multiple functional unit ) . 
اي single processor بنعتبره SISD 
و الفكرة هنا ان ال processor بيجيله single data و بيعملها single instruction  . 

#### SIMD 
الفكرة انك بتاخد اكتر من داتا علي CPUs مختلفه و كلهم بيعملوا نفس ال instruction ، يعني مثلا لو انت عندك داتا حجمها كبير و عايز تعملها filtration فانت بتقسم الداتا دي علي CPUs مختلفه و بيجيلهم نفس الامر instruction ، و ال  instruction دي بتتنفذ لاما sequentially (using pipelining ) او 
parallel  (using multiple processors  )

#### MISD 
هو  مش شائع الاستخدام و بيستخدم في الحاجات الي لازم اتأكد انها مظبوطه جدا زي رحلات الفضاء المكوك . 

#### MIMD 
هو ده الي مستخدم في لابتوباتنا الحاليه ، اهم نقطة فيه اننا لازم نعمل share memory عشان لو فيه two instructions بيعدلو علي نفس ال data . 


### What is meaning of Pipelining ? 
الفكره هي اني عايز استغل كل ال resources بتاعة الجهاز  ، مثال ال 4 اشخاص الي عايزين يشغلوا و بنشفوا و يطبقوا الهدوم بتاعتهم  بدل ما استني كل واحد يخلص الاربع عمليات و بعدين اخش بعديه ، انا ممكن استني لحد ما يخلص غسيل هدومه و بعدين اخش وراه اغسل هدومي  و  اول لما يخلص تنشيف هدومه اخش وراه في التنشيف يعني مستناش لحد ما يخلص العمليات كلها  . 


**خلي بالك** : طريقة حساب الوقت المستغرق في ال pipeline بتشوف مين الي هياخد وقت اكبر في ال stage الحالية و تاخده هو بس ، طب ليه ؟ عشان انت عندك في ال time clock بيدي وقت علي حسب المهمة الي محتاجه وقت اكتر حتي لو المهام التانيه خلصت قبله لازم تستناه لحد ما المهمه الي محتاجه وقت اكبر تخلص ، عشان ال system لازم يكون synchronized . 
يعني لو جينا علي المثال الي عندنا ده ، احنا عندنا 6 stages 
اول واحده هتاخد 30 + التانيه هتاخد 40 + التالتة هتاخد 40 + الرابعة 40 +  الخامسة 40 + السادسة 20  = 
equal = 30 + 40 + 40 + 40 + 40 + 20  = 210 minutes / 60 = **3.5 hours** 

**عملية ال pipelining مش بتسرع ال operation ، هي بتعمل overlapped in execution**



----
لحساب ال clock pipeline cycle  
$$
k*t_{p} + {n-1} 
$$

بعد ما بيحصل fully pipelining كل task بتخلص بعد tp

و من اجل حساب ال speed 
$$
S = \frac{t_{m}}{t_{p}}
$$
tp = time pipelined 
tm = time unpipelined 
S = speed 
