---
---

- we use machine learning because (available data + update flexiability + find the pattern  ) 
- first example movie rate -> find the pattern of the user recommendation 
- second example credit approval  
- component of learning : 
1. input (x) 
2. data (dataset) => (x1,y1) , (x2,y2) 
3. output (y) 
4. target function (f(x)) => ideal formula (unknown)
5. hypothesis (h(x))=> (formula to be used ) 
- learning model = learning algorithm + hypothesis set 
- perceptron = simple hypothesis 
- perceptron = the small unit in NN 
- types of learning 
1. supervised learning (input , correct output )  like coin recognition 
2. unsupervised learning (input , ? )
3. reinforcement learning (input , some correct output , grade of the output ) like puzzle  
-  $\mu$ (out sample error Eout) = unknown target , $\nu$ (in sample error Ein)  = hypothesis (take sample size = N)
- the model is feasible if the  $\nu$ distribution is the same distribution of the $\mu$
- in Hoeffiding inequality if N is large (up to 98%) ... $\nu$  will be close to $\mu$ 
- verification mean apply probability distribution on one hypothesis . 
- [solution of the probability problem toss coins](https://chatgpt.com/c/677e970c-702c-800a-a622-08e0e535120f)
- 10 x 0.5 = 0.5 + .5 + .5 + .5  + ... 
- $0.5^{10}$ = 0.5 x .5 x .5 x .5 x ..... 
- using feature extraction to mnimize the size of the input size and focus on the useful input features 
- add more features (special if it not relevant or training on noisy data) that make it is harder for the model to generalize and cause to overfitting 
- there are two types of technique to find  a separating hyperplane for linear separable data  : 
1. PLA => can use it in just linear separatable data , update weights until all points are correctly classified , if the data is not separable PLA will never converge and will update the weights indefinitely . (الي ما لا نهاية) 
2. POCKET => can use it in both separatable or not separatable data ,it keep track the best weights  and update weights  only when a better solution is found , in non linear it will stop after a number of iterations and give us the best weight during this iterations . 
- pseudo inverse (x tag) : used common if the matrix not invertable or not square , and used common in machine learning when the linear equation not have one solution 
- we transform the non - linear function to linear function using weight (because the linearity of weights ) ...  XOR  problem
- confusion matrix (error matrix) used to solve statistical classification  problems (like hard to classify weak category , hard to measure the performance of a classifier  , misscalssification )
- we test the model on the data from the same distribution of the training dataset (the same probability distribution)
- super market verify fingerprint example (the bad case is false negative )
- CIA fingerprint example (the bad case is false positive)
- Error measure measuring the fit of the model . 
- when the user not specify error measure we can choice : 
1. plausible choice like square error == gaussian noise 
2. friendly choice like closed form or convex optimization 
- reduce error = make g(x)  more generalized and closed to target funtion f(x) 
- Noisy target : mean more than one output on the same  input point (mutually exclusive)  , this mean the target will be not deterministic 
- the diff between multi label classificatoin and Noisy target is : 
1. classification : one input -> two output independantly and not mutually exclusive  
2. noisy target : one input -> two output (mutually exclusive) , because noise  or human error 
- we can solve problem Noisy target using target distribution (soft labels ) , example on target distribution : For example, if you have an image of a blurred dog, the true label might be a distribution: 0.7, 0.3 ("dog" 70% and "cat" 30%)  , The model might predict 0.8, 0.2 (80% "dog", 20% "cat"). Since the prediction is close to the true distribution, it’s a valid prediction.
- the goal of target distribution is to help the model to adapt to uncertrainty in the labels and make robust prediction despite noise or ambiguity . 
- Conformal Prediction (Confidence Master 😎) use confidense level , mean give us a set {"dog" , "cat" } and tell us the true category will not be outside this set  with specific confidense level (95% , for example )  
- when the model will  be complex is not always be good , for example when increase the complexity of the model ..  Ein will be reduced but that  caused to overfitting and increase the gap between the Ein and Eout (Eout - Ein  , is very high) 
- we want replace the M in the Hoeffiding inequality because not overlapped data (mean the training dataset and testing dataset is not from same distribution ) lead to undetemines generalization .     
- Dichotomies : mini hypotheses  => بتحاول تحجم الجزء الي علي اليمين من المعادلة 
- breakpoint : the dataset set can't be shatterd more than 
- any breakpoint is polynomial in N . 
- linear regression aim to predict dependent variables 
- ROC graph (Recall , type 1 Error ) => for binary classification 
- Precision/Recall graph => for Multiclassification 
- w dim : d+1 * 1 
- x dim : d+1 * 1 
- y dim : N * 1
- the aim of the bias is to shift the decision boundary 
- H set : is set of candidate hypothesies to approximate f 
- the condition that must be satisfy is achieve a balance between variance and bias . 
- hypotheses  set is too small -> high bias . 
- when increase the size of N the bound size of the Hoeffiding Inequality become **tighter** (the deviation decreased )
- increae the size of hypotheses set is bad , because $P(E(in)-E(out) > \epsilon)$ will be large ... so we choose just condidate funtions not all available function . 
- 
----
- rules : 
1. 
2. 
3. 
4. 
5. 
6. 
7. 
8. 
9. $sign(w^{T}x)$
10. precision :  $TP / TP+FP$ calculate the true positive that model can classify it from positive prediction 
11. Recall (Sensitivity) :  $TP / TP + FN$ claculate how well the model capture Actual true postive 
12. type || error (miss Rate) = 1 - Recall 
13. Specifity : $TN /TN + FP$ calculate how well the model capture the actual true negative 
14. type | error (false  alarm) = 1-  Specifity
15. F1 score : (use harmonic mean )  , $2\frac{P*R}{P+R}$ 
16. Accuracy : TP + TN / Total (TP + FN + TN + FP)
17. in linear regression (square error ) :  
18. in classification  (binary error ): 
19. target distribution : P(y | x ) 
20. the data (x, y ) or p(x,y) : joint distribution P(x) P(y|x) like the (the input , correct distribution output )\
21. y (target distribution ) = P(y | x ) == F(x) + noise 
22. noise  = y - F(x)
23. F(x) = E(y|x) , deteministic part , excepeted value of y given x 
24. $m_{H}(N)$ = max |H(x1 , x2 , x3) | 
25. positive rays => $m_{H}(N)$ = N+1 (the best )
26. postive intervals => $m_{H}(N)$ = $\frac{1}{2} N^2 + \frac{1}{2} N + 1$
27. convex sets => $m_{H}(N)$ = $2^N$
28. positive rays breakpoint => k =2 
29. positive interval breakpoint => k = 3 
30. convex sets breakpoint => infinity 

---
- diagrams 
1. 
2. 
3. 
4. 
