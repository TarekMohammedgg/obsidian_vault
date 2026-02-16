---
---

why we use machine learning  ? 
1. difficult to track the updates mathmatically (rules)
2. the data is available 
3. find the pattern 
---
First example on machine learning is predicting rate (movie rating) : recommend movie for the viewer depending learn viewer rate . 

----

Second example : credit approval  ... create a model classify if  the user can approve the debit or not ? 

----

component of learning : 
1. input  (x)  => customer application 
2. output  (y) => (good / bad )
3. target function (ideal credit approval formula) (unknown)
4. Data {(x1,y1) , (x2, y2 ) , ... } =>  (historical data about the user)
5. hypothesis   => (formula to be used ) 

---
the learning model = hypothesis set  + learning algorithm (tester man )
test each hypothesis using algorithm 

- ---
simple hypothesis = perceptron 
perceptron just apply on line separatble data 
take the input customer  attributes and apply the next 

but we can written it as : 






x0 = 1 , always 
in vector form 


in the training level : 

training on Data (history of the user data ) 
pick the missclassified data and update the value of the weight 
$$
sign(W^T X) \neq y $$
$$
w =: w + y_{n} *  x_{n}
$$
$y_{n} :$ have two value {-1 , 1 }

---
the types of learning 
1. supervised  learning => (input , correct output ) , like coin recognition 
2. unsupervised learning => (input , ? ) 
3. reinforcement learning => (input , some output , grade of this output ) , like puzzle 

----
is learning is feasible ? this mean is the learned model can use it in real world and work effectively ? 
we can apply this model in the real world if the data that he is training on is close to the real world (close in distribution)

bin marbels example $\mu$ is the  population distribtuion (unknow target ) , when take N marbels independently from the population distribtuion , we get $\nu$ 

so if the $\nu$  is very close to the $\mu$  , this mean the learned model is feasible to apply it on the real world problems 
if no , that mean can't apply it and need more modifications 

Hoeffiding's Inequality 


if N is large that is good , because this mean the $\nu$   is close to $\mu$  distribution 
but take care if we take very very large N this mean we don't do any thing ,because the value of $\nu$  is equal or so so close to the 
$\mu$   , the available rate up to 98% 


so , the learning diagram wil be : 


----

previouse we apply the probability distribution on the one hypothesis  that mean we "verificate " of hypothesis 

one hypothesis mean one $\nu$  distribution 

we want to choose from many hypothesis 

relate it to the learning : 

$\nu$  : in sample error $E_{in}(h)$ => like training error 
$\mu$  : out sample error $E_{out}(h)$ => like testing error on the real world 



معني تلك المعادلة هو ان احتمالية  الفرق بين الخطأ داخل العينة الي الخطأ خارج العينة ان يتخطي قمية ال  ϵ اصغر من او يساوي ال right side . 


10 x 0.5 = 0.5 + .5 + .5 + .5  + ... 
$0.5^{10}$ = 0.5 x .5 x .5 x .5 x ..... 
[solution of the probability problem toss coins](https://chatgpt.com/c/677e970c-702c-800a-a622-08e0e535120f)
steps : 
1. احسب احتمالية ان كوين واحده تجيب 10 رؤوس وراء بعض 
2. و بعدين اطرحها من 1 عشان تجيب احتماليه انها متجبش 10 رؤوس وراء بعض 
3.  احنا حسبناها علي واحد بس باقص بقي نعملها علي ال 1000 

the Hoeffiding inequality for multiple hypothesis (is not overlapped ) : 



----
we use feature extraction to mnimize the size of input data (x) and focus on the useful input features  . 
add more features (special if it not relevant or add noise to the data ) that make it is harder for the model to generalize and cause to overfitting 

----

there are two types of technique to find  a separating hyperplane for linear separable data  : 
1. PLA => can use it in just linear separatable data , update weights until all points are correctly classified , if the data is not separable PLA will never converge and will update the weights indefinitely . (الي ما لا نهاية) 
2. POCKET => can use it in both separatable or not separatable data ,it keep track the best weights  and update weights  only when a better solution is found , in non linear it will stop after a number of iterations and give us the best weight during this iterations . 
----
Classification and Regression 
linear regression 

how to measure the error ? 
we will use square error 

pseudo inverse $X^{†}$ = $(X^{T}X)^{-1} X^{T}$
pseudo inverse used when the matrix is not iversible or if the matrix is not squared (the number of rows not equal the number of columns )  , and used common to solving systems of linear equations that not have uique solutions . 
(يعني احنا بنتحايل علي المصفوفة عشان نعملها ترانسبوز )



 $X^{†}$ dimension = d+1 x N
 
----
use linear regression (real valued) in classification : 
$sign(w^{T}x)$

---
tranform the non - linear function to linear function using weight ,because the linearity of the weight  ... so the weights is not transformed 
XOR  problem 



---
confusion matrix (known as Error matrix ) can solve the problem of statistical classification  . 
statistical classification problem like : 
1. misclassification . 
2. hard in calssify weak category . 
3. hard when measure the performance of a classifier . 
the confusion matrix solve this problem by : 
TP 
TN 
FN 
FP 

precision :  $TP / TP+FP$ calculate the true positive that model can classify it from positive prediction 
Recall (Sensitivity) :  $TP / TP + FN$ claculate how well the model capture Actual true postive 
type || error (miss Rate) = 1 - Recall 
Specifity : $TN /TN + FP$ calculate how well the model capture the actual true negative 
type | error (false  alarm) = 1-  Specifity
F1 score : (use harmonic mean )  , $2\frac{P*R}{P+R}$ 

----
Measure the Error (take the average)
in linear regression (square error ) :  

in classification  (binary error ): 



we test the model on the data from the same distribution of the training  dataset (the same probability distribution )

Examples : 
1. super market verifies fingerprint for discount (false negative is so bad ) 
2. CIA verifies fingerprint for security (false positive is so bad) 

the error measure must be specified by the user 
and if not do it we can choice the next : 
1. plausible choice : square error (linear regression) = Gaussian noise 
2. Freindly measures : closed form or convex optimization 



reduce error = make g(x)  more generalized and closed to target funtion f(x) 

---
Noisy target : mean more than one output on the same  input point (mutually exclusive)  

this mean the target function is not deteministic 

what is the diff between Noisy target and Multi label classification ? 
Noisy target : one input have two outputs (two labels ) , because noise , human error ..... the two outputs can be mutually exclusive (يتعارض وجودهما مع بعض ) .
يعني ممكن الموديل يطلعلي ان المدخل الي دخلته ليه قطه و كلب مع بعض   . 

Multiclassification label : one input have two independent (distinct ) targets (labels ) this mean (not mutually exclusive) 
يعني ممكن الموديل يطلعلي ان المدخل الي دخلته ليه قطه  و بيضاء (حاجتين لا يتعارض وجودهما مع بعض )  . 


 Noisy Target and Target Distribution (Soft Labels): 
Noisy target means the true label is uncertain or ambiguous due to factors like noise, blurriness, or human error.

For example, if you have an image of a blurred dog, the true label might be a distribution: 0.7, 0.3 ("dog" 70% and "cat" 30%).

The model might predict 0.8, 0.2 (80% "dog", 20% "cat"). Since the prediction is close to the true distribution, it’s a valid prediction.

The goal of using target distributions is to help the model adapt to uncertainty in the labels and make more robust predictions despite noise or ambiguity . 


Conformal Prediction (Confidence Master 😎)معيار قياس 

Conformal prediction provides prediction sets instead of a single label. These sets contain all possible labels with a specific confidence level (e.g., 95% confidence).

Given a model's prediction, conformal prediction generates a set of labels, e.g., {"dog", "cat"}, and guarantees that the true label will be inside this set with 95% confidence.

The key idea is to provide a valid confidence interval or set for the predicted labels

target distribution : P(y | x )
the date (x, y ) or p(x,y) : joint distribution P(x) P(y|x) like the (the input , correct distribution output )

y (target distribution ) = P(y | x ) == F(x) + noise 
F(x) = E(y | x ) : the deterministic part , excepected value of y given x 
noise = y - f(x) 


---

we want to apply balance , when increase the complexity of the model Ein will be reduced but that be caused to overfitting and increase the gap between the Ein and Eout (Eout - Ein  , is very high) 


----

now  we want replace the M in the Hoeffiding inequality  
because not overlapped data (mean the training dataset and testing dataset is not from same distribution ) lead to undetemines generalization .            

Dichotomies : mini hypotheses 
بتحاول تحجم ال range بتاع ال right side في  heoffiding inequality بدل ما تكون infinity هتبقي $2^N$ 

the growth function counts the most dichotomies الثنائيات on any N points : 
$m_{H}(N)$ = max |H(x1 , x2 , x3) | 

1. positive rays => $m_{H}(N)$ = N+1 (the best )
2. postive intervals => $m_{H}(N)$ = $\frac{1}{2} N^2 + \frac{1}{2} N + 1$
3. convex sets => $m_{H}(N)$ = $2^N$

---
breakpoint : the data set can't be shatterd more than 
1. positive rays => k =2 
2. positive interval => k = 3 
3. convex sets => infinity 

any break point is polynomial in N 
