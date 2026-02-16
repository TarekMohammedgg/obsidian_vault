---
---


dev set = validation set = development set

**definition** : to check accuracy of different models

الطريقة كالأتي :

we select the best model between some models using training and dev sets after that using testing set to check the actual performance of the model .

so ,  
**training set** : used to train the model .  
**validation set** : used to tune hyperparameters and select the best model .  
**test set** : used only once for the final evaluation after the model is fully trained and tuned .

### 

what is the different between [cross validation](_zettlenotes/other-notes/cross-validation.html) and [Regularization](_zettlenotes/programming-notes/ai-notes/regularization.html) ?

**Regularization**  
reduce overfitting by add a penalty  
**Cross validation**  
try to add advise and lead the model to correct roadmap (tuning parameters)  
is a check point to ensure the model is learning effectively and generalizing well to new data