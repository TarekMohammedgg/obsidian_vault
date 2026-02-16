---
---
#ml_and_dnn 

( $\alpha$ , $\beta$ ,  # hidden layers , # hidden units , learning decay , mini-Batch size  )

## how to search systematically on Good hyperparameters 
### use Random Search (Not Grid search)  
لانه بيديك قابلية للبحث بشكل مكثف و لأنك في الامثلة العملية ممكن تتعامل مع كم كبير من ال dataset . 

### Coarse to fine 
الفكرة هنا عند التركيز علي نقطة معينة محاولة اخذ المساحة المحيطة بها و تدقيق البحث اكثر فأكثر للحصول علي قيم دقيقة و فعالة . 
