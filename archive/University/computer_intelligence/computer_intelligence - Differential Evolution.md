- زي ال [[Genetic Algorithm]] و لكن بتركز اكتر علي ال [[mutation]] اكتر من ال [[recombination - crossover]]

- Differential Evolution : 
1. handle non-linear , Multimodal 
2. *Parallelize* (independently)
3. solution in genetic algorithm == Vector in Differential Evolution 

-----
- كل Vector في ال Population لازم يبقي مرة واحده علي الاقل Target vector . 


- بقارن ال Trial vector مع ال target vector و اشوف لو ال fitness مين الاحسن . 

*Implementation the crossover of mutant vector   with target vector:*


```c++
// crossover rate (cr)  

if(Math.Random > cr) {
target_vector ;
}else {
mutant_vector ; 
}
```

- الناتج من ال if condition دي هيبقي Trial Vector ، بعدين هنشوف ال fitness بتاعة ال Trial vector و ال Target vector و الاحسن هنحطه في ال population الجديدة . 






----
- DE => as a local Searcher 
- GA => as a Global Searcher 
- GA find the peaks and DE find the highest point of the peak 

