---
---
#ml_and_dnn 
Batch : يقوم بمعالجة البيانات دفعة واحدة 

Mini-batch : يقوم بتقسيم البيانات الي دفعات صغيرة و يتعامل معها علي حدي 

```python 
x(i) => Example Number 
z[b] => Layer Number 
x{t} , y{t}  => رقم المجموعة الصغيرة المستخدمة في ال 
				mini-batch 
```

**vectorization** : يسرع من عملية المعالجة ، و لكن لا يحدث فرق كبير مع ال 
				large dataset 

----
### Training with mini-batch gradient descent 
```python 
(x{i} , y{i}) = (x,,y)
```
if mini-batch size = M : batch gradient descent 
if mini-batch size = 1 : stochastic GD (Every example is it own ( x,(i) , y(i) )


---
### Stochastic GD vs. Batch GD 

**Stochastic** 
x lose speedup for vectorization => 
ال Optimization مش بيوصل الي ال Minimum و لكن بيكون حوليه . 

**In between (mini-batch size is not too large (small )**
Fastest learning 
- Vectorization 
- make progress without Needing to wait 

**Batch GD (mini-batch size = M)** 
x too long per iteration 

----
### Choosing your mini-Batch size  
if small training set : use batch GD 
typical mini-batch size : 2^[ ] (64 , 128 , 256) 
make sure mini-batch fit in cpu (GPU memory ) 

---
### Exponentially weighted Average 

```python 
v(t) = B * v(t-1) + (1-B) * theta(t) 
```

parameters : 
- v(t) : approximately average over => $\frac{1}{1-\beta}$ days temperature 