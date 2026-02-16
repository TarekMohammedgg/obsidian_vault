**[Video link](https://www.youtube.com/watch?v=6rDGCwBdQs0)

  

# Basics 

---

#### What is the different between .Net Framework vs. .Net core ? 

.Net framework is running on Windows OPerating system 

.Net core can run on different operating systems like [ Linux , Mac ] 

  

#### What is the main advantage of c# ? 

The main advantage is can used wit the next fields like [ machine learning and deep learning - desktop application - mobile - web services - gaming - and so on ]

  

####  ال solution ممكن يكون ليه اكتر من project 

  

#### Why we using console application when learning c# ? 

عشان من الاخره بيطلعلك صفحة بيضا و انت بتبقي مركز علي تعلم ال C#  

  

في الجزئية الخاصة بالاعداد العشرية عندنا 3 data tyes و ال by default بتاعي بيكون double 

  

|                                                                                |
| ------------------------------------------------------------------------------ |
| float x = 1.2F  <br>decimal x = 1.2M  <br>double x = 1.2 // or double x = 1.2D |

|   |
|---|
|intVar = (int) doubleVar|

  

#### Type conversation plus ( parse and convert class ) 

Parse => parsing happened on runtime 

  

|   |
|---|
|string age = "25" ;  <br>int intVar = int.Parse(age) ;  <br>Console.WriteLine(intVar) ;|

  
  

Convert class

  
  

---

  

#### Rules For Naming Variables in C# 

![|0x0](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeERXt_8gxEBrJJIBziOffditLZxc50kvkl7ZeRFjCRl9yMwASL4T3JG_u26IGSsj-gpVz-JCOKzeFNwy-vFwJF9YTya0KKA2s6ztQv78ieJZsidBExnyoZ1TNb6kxz6x-5abrpoQ?key=u7HRodpDRmTKZgu72x4KSQ)

  
  

# OOP in C# 

#### What is the diff between Programming Paradigm ? 

![|654x257](https://lh7-rt.googleusercontent.com/docsz/AD_4nXewo2JWcIbqgFQJik5WdalMauAOa9zowjK3RGyN_ggk6N3ps9JjSHMr392bAroZ2lZGLB2NcP6a1sVO_OSZtVNfysyZQeBQ5dqxt1WgAkLWLAxuTmAfD5YgI8DMVbxTx-kxojgw?key=u7HRodpDRmTKZgu72x4KSQ)

  

#### Pass by reference and Pass by value ? 

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeugyoTQG6354Do68QFT31lNuF3wahyb3OEd1BNhH-H4BwineRQ6t_zYe7qeSID-ob3ba9IjXatsVbZNJBJSKo6ohAkpiXgCbI4pqP2R_lbOQ9jsMlGGAwxVUTmkex-ILEy11_9GA?key=u7HRodpDRmTKZgu72x4KSQ)

  
  

# Advanced Topics in C# 

#### What is Struct in C# and what is the diff between class ? 

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfHM1xMvCktyW66bSFndrmn-QZGgpOeic-n-Fdy6VWWBA--F2Wa9wBtMWAz4p3CTqWkc7fCkDhLiEHpJUM4GXFvzk_V5_7iXFZZLUSDYvEtApZsqLLzH8b1o1NK4V3VhigSQVYV?key=u7HRodpDRmTKZgu72x4KSQ)

  

#### What is the diff between Mutable and Immutable object ? 

Immutable like String in c# 

Can not change it in runtime 

The usage of Immutable object for thread safety and async operations 

لان بالشكل ده الكود بتاعك اقل عرضة للخطأ و كمان ده بدوره بيعلي ال performance بتاعة التطبيق و كمان بتقدر تحقق مبدأ ال Encapsulation بشكل افضل . 

Mutable 

Can change it in runtime 

بقدر اقول علي الحاجه دي mutable لو ال Internal state بتاعتها قابله للتغيير بعد الانشاء زي ال double and int

The usage of mutable object for memory usage . 

يعنيي اقدر اغير في القيمة بتاعتي بدل ما اروح انشأ ليا مكان جديد في ال memory  

  

#### Why we use Interfaces ? 

- Provide Loose coupling 
    
- Can apply multiple inheritance using interface 
    

  

#### Interfaces vs. class ? 

![|654x348](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfUSg3NTDGOspX7__eZk1GsAAG39yQYS9snc7DLjWxXqFC95GbxU1Dqjisg1ZhmGIQlQ23UjqMi58HUMuAwkk6W7mKvAiwwllGF2tDXGkm4OtVIsu6f19d99cpRCHPAMKvJzGKTog?key=u7HRodpDRmTKZgu72x4KSQ)

#### IEnumerable Vs. IQueryable ? 

They are two interfaces in C# 

IEnumerable : لو جيت  تجيب الداتا من الداتا بيز  و طبقت عليها شوية فلتر ، هو هيجيب الداتا كلها  و يخزنها في الميموري و بعدين يطبق الفيلتر بتاعك في الميموري 

IQueryable:   لما تيجي تجيب داتا من الداتا بيز و تطبق عليها فلتر ، الفلتر بيتنفذ في الداتا بيز قبل ما تروح للميموري ، معني كده ان الميموري بتشيل الشكل النهائي من غير ما يحصل اي عمليات داخل الميموري علي عكس الي حصل في النوع الاول 

- Where code tranfered to Expression code 
    
- Then send the expression to the EF core(db provider ) 
    
- The ef core transfer the where code to SQL code and get the filtered data in the memory without doing any operations in memory . 
    

#### What is Delegate  ? 

Pointer as a Function , behind the seen the delegate function  is a class in C# 

Is  a pointer point to function (get the reference of the function and store it ) . 

#### What is generics and how to create your own generic class and function 

#### Learn about Linq ? 

#### Learn about record in c# 9 

#### Async and await  in C# ?**