### **Supervised Learning**

### **1. Introduction to Supervised Learning**

- **Definition:** A type of machine learning where the model learns from a labeled dataset. This means the input data (features) is paired with the correct output (labels or targets).
- **Goal:** To learn a mapping function from input features to output labels so that the model can accurately predict outputs for new, unseen data.
- **Categories:**
    - **Classification:** Predicts a discrete (categorical) output label.
    - **Regression:** Predicts a continuous (numerical) output value.
- **Key Concept:** The model learns from "known categories" or "known classes."

### **2. Classification vs. Clustering**

- **Classification (Recognition / Supervised Classification):**
    - Uses **known categories**.
    - Example: Distinguishing between Category "A" and Category "B" based on labeled examples.
    - Input includes records with attributes, one of which is the _class_ (classifier).
    - Goal: Find a model for the class attribute as a function of other attributes.
- **Clustering (Unsupervised Classification):**
    - Uses **unknown categories**.
    - Groups similar data points together without prior knowledge of classes.
    - This is a concept briefly introduced in the supervised handout as a contrast.

### **3. Other Related Pattern Recognition Tasks**

- **Association Rule Discovery:**
    - Given records containing sets of items.
    - Produces dependency rules that predict occurrences of one item based on others (e.g., "If a customer buys item X, they are likely to buy item Y").
- **Regression Analysis (An Early Task):**
    - A statistical process for estimating relationships among variables.
    - Includes techniques for modeling and analyzing several variables.
    - Focuses on predicting a continuous outcome.

### **4. Pattern Recognition Applications (Examples)**

|Problem Domain|Application|Input Pattern|Output Label|
|---|---|---|---|
|**Document Analysis**|Optical Character Recognition|Handwritten/Printed Text|Character Class|
||Speech Recognition|Voice|Spoken Word|
|**Biometrics**|Fingerprint Identification|Fingerprint|Identity|
||Face Recognition|Face Image|Identity|
|**Medical Diagnosis**|Cancer Detection|Medical Images|Cancer/No Cancer|
|**Financial**|Fraud Detection|Transaction Data|Fraudulent/Legitimate|
||Stock Market Prediction|Historical Stock Data|Stock Price|

### **5. Steps in Supervised Learning**

1. **Data Collection:** Gather relevant data.
2. **Data Preprocessing:** Clean, transform, and prepare the data (e.g., handling missing values, normalization).
3. **Feature Engineering:** Select or create relevant features from the raw data.
4. **Data Splitting:** Divide the dataset into training and testing sets (e.g., 80% training, 20% testing).
    - **Training Set:** Used to train the model.
    - **Testing Set:** Used to evaluate the model's performance on unseen data.
5. **Model Selection:** Choose an appropriate machine learning algorithm (e.g., k-Nearest Neighbors, Decision Trees, Support Vector Machines, Logistic Regression, Naive Bayes).
6. **Model Training:** The chosen algorithm learns patterns from the training data.
7. **Model Evaluation:** Assess the model's performance on the testing set using various metrics.
8. **Hyperparameter Tuning:** Adjust the model's hyperparameters to optimize performance.
9. **Deployment:** Integrate the trained model into an application.

### **6. k-Nearest Neighbors (k-NN) Algorithm**

- **Concept:** A non-parametric, lazy learning algorithm used for both classification and regression. It classifies a new data point based on the majority class of its 'k' nearest neighbors in the training data.
- **"Lazy Learner":** It does not explicitly learn a model during the training phase. Instead, it memorizes the training data and performs computations only when a prediction is requested.
- **Steps for Classification:**
    1. **Choose k:** Decide the number of neighbors (k).
    2. **Calculate Distance:** Calculate the distance (e.g., Euclidean distance) between the new data point and all data points in the training set.
    3. **Find k-Nearest Neighbors:** Identify the 'k' data points from the training set that are closest to the new point.
    4. **Vote for Class:** For classification, assign the new data point to the class that is most frequent among its 'k' nearest neighbors.
    5. **For Regression:** For regression, assign the new data point the average of the values of its 'k' nearest neighbors.
- **Distance Metrics:**
    - **Euclidean Distance:** The most common metric for continuous features.
    - Manhattan Distance, Minkowski Distance, etc. (Other metrics can be used based on data type and problem).
- **Choosing the Optimal `k`:**
    - **Small `k`:** Can be sensitive to noise/outliers (overfitting). High variance, low bias.
    - **Large `k`:** Smoothes out predictions but might ignore local patterns (underfitting). Low variance, high bias.
    - **Common Practice:** Use cross-validation or observe the accuracy on a validation set for different `k` values. Often, an odd `k` is preferred in classification to avoid ties.
    - **Graph Analysis:** Plotting training accuracy and testing accuracy against different `k` values helps visualize the trade-off. A high value for `k` can lead to good testing accuracy, as shown in the example (k=9 yielding 0.73 accuracy).
- **Example Code Snippets (Illustrative, based on handout):**
    - **Import necessary libraries:** `numpy`, `matplotlib.pyplot`, `sklearn.neighbors.KNeighborsClassifier`, `sklearn.model_selection.train_test_split`.
    - **Data Splitting:** `X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)` (Example `test_size=0.2` implies 20% for testing).
    - **Initializing `k` values:** `my_neighbors = np.arange(1, 10)` (range of k from 1 to 9).
    - **Accuracy arrays:** `train_acc = np.empty(len(my_neighbors))`, `test_acc = np.empty(len(my_neighbors))`
    - **Looping through `k` values:**

```jsx
for i, k in enumerate(my_neighbors):
knn_model = KNeighborsClassifier(n_neighbors=k)
knn_model.fit(X_train, y_train)
train_acc[i] = knn_model.score(X_train, y_train)
test_acc[i] = knn_model.score(X_test, y_test)
* **Plotting Results:**python
plt.title('k-NN with different No of neighbors')
plt.plot(my_neighbors, test_acc, label=' Testing Accuracy ')
plt.plot(my_neighbors, train_acc, label=' Training accuracy ')
plt.legend()
plt.xlabel('No of neighbors')
plt.ylabel('Accuracy of model')
plt.show()
```

- **Final Model Selection (Example):** knn_model = KNeighborsClassifier(n_neighbors=9), knn_model.score(X_test, y_test) (Result: 0.73 accuracy for K=9).

```

### **7. Other Supervised Learning Algorithms (Brief Mention)**

- **Support Vector Machines (SVM):** A powerful algorithm for classification and regression that finds the optimal hyperplane to separate data points.
- **Decision Trees:** Tree-like models that make decisions based on features to classify or predict.
- **Logistic Regression:** A statistical model used for binary classification.

### **Unsupervised Learning**

### **1. Introduction to Unsupervised Learning**

- **Definition:** A type of machine learning where the model learns from unlabeled data. The algorithm must find patterns, structures, or relationships in the data without any prior guidance on the correct output.
- **Goal:** To discover hidden patterns or intrinsic structures in input data.
- **Key Concept:** Deals with "unknown categories" or "unsupervised classification."

### **2. Clustering Algorithms**

- **Definition:** The task of grouping a set of objects in such a way that objects in the same group (called a cluster) are more similar to each other than to those in other groups (clusters).
- **Types of Clustering Algorithms:**
    - **Hierarchical Algorithms:**
        - Create a hierarchical decomposition of the set of objects.
        - Can be **Agglomerative** (bottom-up: start with individual points and merge clusters) or **Divisive** (top-down: start with one cluster and split).
    - **Partitional Algorithms:**
        - Construct various partitions of the data and then evaluate them using some criterion.
        - **Non-hierarchical:** Each instance is placed in exactly one of K non-overlapping clusters.
        - User typically needs to input the desired number of clusters (K).
        - Examples: k-means, k-medoids.

### **3. k-means Algorithm**

- **Type:** A partitional clustering algorithm.
- **Objective:** To partition `n` observations into `k` clusters, where each observation belongs to the cluster with the nearest mean (centroid), serving as a prototype of the cluster.
- **Distance Metric:** Commonly uses Euclidean Distance.
- **Algorithm Steps:**
    1. **Decide on a value for `k`:** Determine the number of clusters you want to form.
    2. **Initialize `k` cluster centers (centroids):**
        - These can be initialized randomly (e.g., picking `k` random data points as initial centroids).
        - Or by selecting `k` data points that are furthest apart or using more sophisticated methods (e.g., k-means++).
    3. **Assign objects to the nearest cluster center:**
        - For each data point, calculate its distance to all `k` centroids.
        - Assign the data point to the cluster whose centroid is closest.
        - This step decides the "class memberships" of the `N` objects.
    4. **Re-estimate the `k` cluster centers:**
        - Recalculate the new centroid for each cluster.
        - The new centroid is typically the mean of all data points assigned to that cluster.
        - Assumes the memberships found in step 3 are correct.
    5. **Check for Convergence:**
        - If none of the `N` objects changed their cluster membership in the last iteration, the algorithm has converged, and you exit.
        - Otherwise, go back to step 3 and repeat the assignment and re-estimation process.
- **Characteristics:**
    - Simple and computationally efficient.
    - Sensitive to initial centroid placement (can lead to different results).
    - Requires `k` to be specified in advance.
    - Assumes clusters are spherical and equally sized.
    - Sensitive to outliers.

### **4. DBSCAN (Density-Based Spatial Clustering of Applications with Noise)**

- **Type:** A density-based clustering algorithm.
- **Key Idea:** Clusters are dense regions of points that are separated by regions of lower density. It can find arbitrarily shaped clusters and identify noise/outliers.
- **Parameters:**
    - **`Eps` (ε):** The maximum radius of the neighborhood to consider for a point. It defines how close points must be to each other to be considered part of a cluster.
    - **`MinPts`:** The minimum number of points required to form a dense region (a core point).
- **Core Concepts:**
    - **`NEps(p)` (ε-neighborhood of point p):** The set of all points `q` in the dataset `D` such that the distance between `p` and `q` is less than or equal to `Eps`. `NEps(p) = {q ∈ D | dist(p,q) ≤ Eps}`.
    - **Core Point:** A point `q` is a core point if its ε-neighborhood (`NEps(q)`) contains at least `MinPts` number of points (including `q` itself). This means `|NEps(q)| ≥ MinPts`.
    - **Directly Density-Reachable:** A point `p` is directly density-reachable from a point `q` (w.r.t. `Eps`, `MinPts`) if:
        1. `p` belongs to `NEps(q)`.
        2. `q` is a core point (`|NEps(q)| ≥ MinPts`).
        - This implies `p` is in the neighborhood of a core point `q`.
    - **Density-Reachable:** A point `p` is density-reachable from a point `q` (w.r.t. `Eps`, `MinPts`) if there is a chain of points `p1, ..., pn` where `p1 = q`, `pn = p`, and `pi+1` is directly density-reachable from `pi`.
        - This defines a connection through a series of core points.
    - **Density-Connected:** A point `p` is density-connected to a point `q` (w.r.t. `Eps`, `MinPts`) if there is a point `o` such that both `p` and `q` are density-reachable from `o`.
        - This means `p` and `q` belong to the same cluster but might not be directly reachable from each other; they are connected through a common core point.
    - **Noise (Outlier):** Objects that are not directly density-reachable from at least one core object. These points are not part of any cluster.
- **DBSCAN Algorithm Outline:**
    1. Start with an arbitrary unvisited point.
    2. If its `Eps`neighborhood contains `MinPts` points (it's a core point), a new cluster is created.
    3. Recursively add all directly density-reachable points (and their density-reachable points) to the cluster.
    4. If the point is not a core point, it's temporarily marked as noise (it might become part of a cluster if a core point later makes it density-reachable).
    5. Continue until all points are visited.

---

### **60 Multiple Choice Questions (MCQs)**

**Instructions:** Choose the best answer for each question.

---

**Section 1: Supervised Learning (Q1-Q30)**

1. Which type of machine learning involves learning from a labeled dataset?
a) Unsupervised Learning
b) Reinforcement Learning
c) Supervised Learning
d) Semi-supervised Learning
**Correct Answer: c) Supervised Learning**
2. What is the primary goal of supervised learning?
a) To discover hidden patterns in unlabeled data.
b) To predict output labels for new, unseen data.
c) To find optimal actions through trial and error.
d) To reduce the dimensionality of data.
**Correct Answer: b) To predict output labels for new, unseen data.**
3. In supervised learning, if the output variable is categorical, the task is called:
a) Regression
b) Clustering
c) Classification
d) Dimensionality Reduction
**Correct Answer: c) Classification**
4. If the output variable is continuous, the supervised learning task is called:
a) Classification
b) Clustering
c) Association
d) Regression
**Correct Answer: d) Regression**
5. What is the key characteristic of data used in supervised learning?
a) It is always in image format.
b) It consists of unlabeled data points.
c) It has known categories or labels.
d) It requires real-time processing.
**Correct Answer: c) It has known categories or labels.**
6. Which of the following is an example of a classification application mentioned in the handout?
a) Stock Market Prediction
b) Optical Character Recognition (OCR)
c) Fraud Detection
d) All of the above
**Correct Answer: d) All of the above**
7. Which task focuses on finding a model for a class attribute as a function of other attributes in a training set?
a) Clustering
b) Association Rule Discovery
c) Classification
d) Regression Analysis
**Correct Answer: c) Classification**
8. What is the purpose of the testing set in supervised learning?
a) To train the model.
b) To evaluate the model's performance on unseen data.
c) To perform feature engineering.
d) To collect initial data.
**Correct Answer: b) To evaluate the model's performance on unseen data.**
9. What percentage of the dataset is typically allocated for the training set (as per the example split)?
a) 50%
b) 20%
c) 80%
d) 100%
**Correct Answer: c) 80%**
10. What is `k` in the k-Nearest Neighbors (k-NN) algorithm?
a) The number of clusters.
b) The number of features.
c) The number of neighbors to consider.
d) The learning rate.
**Correct Answer: c) The number of neighbors to consider.**
11. k-NN is considered a "lazy learner" because:
a) It trains very slowly.
b) It does not explicitly learn a model during training.
c) It requires minimal data for training.
d) It can only be used for small datasets.
**Correct Answer: b) It does not explicitly learn a model during training.**
12. Which distance metric is most commonly used in k-NN for continuous features?
a) Manhattan Distance
b) Chebyshev Distance
c) Hamming Distance
d) Euclidean Distance
**Correct Answer: d) Euclidean Distance**
13. In k-NN classification, how is the class of a new data point determined?
a) By averaging the values of its k neighbors.
b) By identifying the most frequent class among its k nearest neighbors.
c) By selecting the class of the furthest neighbor.
d) By calculating the square root of k.
**Correct Answer: b) By identifying the most frequent class among its k nearest neighbors.**
14. A very small value of `k` in k-NN can lead to:
a) Underfitting
b) High bias
c) Sensitivity to noise/outliers
d) Smoother predictions
**Correct Answer: c) Sensitivity to noise/outliers**
15. A very large value of `k` in k-NN can lead to:
a) Overfitting
b) Ignoring local patterns (underfitting)
c) High variance
d) Improved boundary detection
**Correct Answer: b) Ignoring local patterns (underfitting)**
16. What is the role of `knn_model.fit(X_train, y_train)` in the provided k-NN code snippet?
a) To predict labels for new data.
b) To compute the accuracy of the model.
c) To train the k-NN model on the training data.
d) To select the optimal k value.
**Correct Answer: c) To train the k-NN model on the training data.**
17. If `knn_model.score(X_test, y_test)` returns 0.73, what does this indicate?
a) The model has 73% accuracy on the training set.
b) The model has 73% accuracy on the test set.
c) The model is 73% underfit.
d) The model is 73% overfit.
**Correct Answer: b) The model has 73% accuracy on the test set.**
18. What is `random_state` used for in `train_test_split`?
a) To randomly shuffle the features.
b) To ensure reproducibility of the split.
c) To set a random seed for the model.
d) To randomize the target labels.
**Correct Answer: b) To ensure reproducibility of the split.**
19. Which of the following is NOT a common step in the supervised learning pipeline?
a) Data Collection
b) Data Interpretation
c) Model Evaluation
d) Feature Engineering
**Correct Answer: b) Data Interpretation**
20. What is the main purpose of "Hyperparameter Tuning" in supervised learning?
a) To reduce the number of features.
b) To adjust model parameters to optimize performance.
c) To split the data into training and testing sets.
d) To deploy the model.
**Correct Answer: b) To adjust model parameters to optimize performance.**
21. An early task related to pattern recognition that estimates relationships among variables is:
a) Classification
b) Clustering
c) Regression Analysis
d) Association Rule Discovery
**Correct Answer: c) Regression Analysis**
22. What does `plt.legend()` do in the k-NN accuracy plot code?
a) Sets the title of the plot.
b) Displays labels for each plotted line.
c) Defines the x-axis label.
d) Shows the accuracy score.
**Correct Answer: b) Displays labels for each plotted line.**
23. In the context of k-NN accuracy plots, if the training accuracy is very high and testing accuracy is significantly lower, it indicates:
a) Underfitting
b) Optimal model
c) Overfitting
d) Balanced model
**Correct Answer: c) Overfitting**
24. Which supervised learning algorithm is known for finding the optimal hyperplane to separate data points?
a) k-Nearest Neighbors
b) Decision Trees
c) Support Vector Machines (SVM)
d) Naive Bayes
**Correct Answer: c) Support Vector Machines (SVM)**
25. What is the role of `np.arange(1, 10)` when selecting `k` values for k-NN?
a) It creates an array of random integers.
b) It generates a sequence of integers from 1 up to (but not including) 10.
c) It calculates the mean of `k` values.
d) It defines the maximum `k` value.
**Correct Answer: b) It generates a sequence of integers from 1 up to (but not including) 10.**
26. In the provided k-NN plot, what does the x-axis represent?
a) Accuracy of model
b) Training accuracy
c) Testing accuracy
d) No of neighbors (k)
**Correct Answer: d) No of neighbors (k)**
27. If a pattern recognition application is "Speech Recognition," what would be the typical "Input Pattern"?
a) Handwritten Text
b) Voice
c) Fingerprint
d) Transaction Data
**Correct Answer: b) Voice**
28. Which step in supervised learning involves transforming raw data into a suitable format for the model?
a) Model Selection
b) Model Training
c) Data Preprocessing
d) Model Deployment
**Correct Answer: c) Data Preprocessing**
29. What is a common pitfall when choosing a very small `k` value in k-NN?
a) It might lead to underfitting.
b) It makes the model too simple.
c) It can be highly influenced by noisy data points.
d) It is always the best choice for small datasets.
**Correct Answer: c) It can be highly influenced by noisy data points.**
30. In the context of the k-NN graph, what does a high value for `k` generally imply for testing accuracy?
a) It always decreases testing accuracy.
b) It can lead to good testing accuracy.
c) It causes the model to overfit.
d) It makes the model faster.
**Correct Answer: b) It can lead to good testing accuracy.**

---

**Section 2: Unsupervised Learning (Q31-Q60)**

1. Which type of machine learning deals with unlabeled data to find hidden patterns?
a) Supervised Learning
b) Reinforcement Learning
c) Unsupervised Learning
d) Semi-supervised Learning
**Correct Answer: c) Unsupervised Learning**
2. What is the primary goal of clustering algorithms?
a) To predict continuous values.
b) To classify data into known categories.
c) To group similar data points together.
d) To reduce the number of features.
**Correct Answer: c) To group similar data points together.**
3. Which of the following is NOT a type of clustering algorithm mentioned?
a) Hierarchical algorithms
b) Partitional algorithms
c) Regression algorithms
d) Density-based algorithms (implied by DBSCAN)
**Correct Answer: c) Regression algorithms**
4. In partitional clustering, what does the user typically need to input?
a) The desired number of features.
b) The desired number of clusters (K).
c) The learning rate.
d) The distance metric.
**Correct Answer: b) The desired number of clusters (K).**
5. Which clustering algorithm is an example of a partitional algorithm?
a) DBSCAN
b) Hierarchical Agglomerative
c) k-means
d) Spectral Clustering
**Correct Answer: c) k-means**
6. What is the objective of the k-means algorithm?
a) To find the most distant points in a dataset.
b) To partition 'n' observations into 'k' clusters where each observation belongs to the cluster with the nearest mean.
c) To identify outliers in the data.
d) To create a tree-like hierarchy of clusters.
**Correct Answer: b) To partition 'n' observations into 'k' clusters where each observation belongs to the cluster with the nearest mean.**
7. In k-means, what are the cluster centers often referred to as?
a) Nodes
b) Neighbors
c) Centroids
d) Pivots
**Correct Answer: c) Centroids**
8. Which step immediately follows "Decide on a value for k" in the k-means algorithm?
a) Assign objects to the nearest cluster center.
b) Re-estimate the k cluster centers.
c) Initialize the k cluster centers.
d) Check for convergence.
**Correct Answer: c) Initialize the k cluster centers.**
9. How are data points assigned to clusters in k-means?
a) Randomly.
b) To the cluster whose centroid is furthest.
c) To the cluster whose centroid is closest.
d) Based on their density.
**Correct Answer: c) To the cluster whose centroid is closest.**
10. What happens in step 4 of the k-means algorithm?
a) New data points are added.
b) The cluster centers are re-estimated by taking the mean of assigned points.
c) The algorithm checks if any objects changed membership.
d) The value of k is changed.
**Correct Answer: b) The cluster centers are re-estimated by taking the mean of assigned points.**
11. The k-means algorithm exits when:
a) It reaches a predefined number of iterations.
b) None of the objects changed membership in the last iteration.
c) All clusters have only one member.
d) The sum of distances is maximized.
**Correct Answer: b) None of the objects changed membership in the last iteration.**
12. What is a known disadvantage of the k-means algorithm?
a) It can find arbitrarily shaped clusters.
b) It is insensitive to initial centroid placement.
c) It requires `k` to be specified in advance.
d) It handles noise effectively.
**Correct Answer: c) It requires `k` to be specified in advance.**
13. Which clustering algorithm is known for finding arbitrarily shaped clusters and detecting noise?
a) k-means
b) Hierarchical Clustering
c) DBSCAN
d) k-medoids
**Correct Answer: c) DBSCAN**
14. What are the two main parameters for the DBSCAN algorithm?
a) `k` and distance metric
b) `Eps` (ε) and `MinPts`
c) Number of iterations and threshold
d) Cluster count and centroid type
**Correct Answer: b) `Eps` (ε) and `MinPts`**
15. In DBSCAN, what does `Eps` (ε) represent?
a) The minimum number of points in a cluster.
b) The maximum radius of the neighborhood to consider for a point.
c) The minimum distance between two clusters.
d) The desired number of clusters.
**Correct Answer: b) The maximum radius of the neighborhood to consider for a point.**
16. What does `MinPts` in DBSCAN define?
a) The minimum number of clusters.
b) The maximum number of points in an ε-neighborhood.
c) The minimum number of points required to form a dense region (a core point).
d) The minimum distance to a centroid.
**Correct Answer: c) The minimum number of points required to form a dense region (a core point).**
17. A point `q` is considered a "core point" in DBSCAN if:
a) Its ε-neighborhood contains exactly one point.
b) Its ε-neighborhood contains at least `MinPts` number of points.
c) It is density-reachable from another point.
d) It is an outlier.
**Correct Answer: b) Its ε-neighborhood contains at least `MinPts` number of points.**
18. What is `NEps(p)` in DBSCAN?
a) The number of core points.
b) The set of points directly density-reachable from `p`.
c) The set of all points `q` such that `dist(p,q) <= Eps`.
d) The noise points around `p`.
**Correct Answer: c) The set of all points `q` such that `dist(p,q) <= Eps`.**
19. A point `p` is "directly density-reachable" from `q` if `p` is in `NEps(q)` and:
a) `p` is also a core point.
b) `q` is a core point.
c) `p` and `q` are far apart.
d) `MinPts` is 1.
**Correct Answer: b) `q` is a core point.**
20. If there is a chain of points `p1, ..., pn` such that `pi+1` is directly density-reachable from `pi`, then `pn` is __________ from `p1`.
a) Directly density-reachable
b) Density-connected
c) Density-reachable
d) Noise
**Correct Answer: c) Density-reachable**
21. What does it mean if a point `p` is "density-connected" to a point `q` in DBSCAN?
a) `p` is directly density-reachable from `q`.
b) `q` is directly density-reachable from `p`.
c) Both `p` and `q` are density-reachable from a common point `o`.
d) `p` and `q` are core points.
**Correct Answer: c) Both `p` and `q` are density-reachable from a common point `o`.**
22. In DBSCAN, objects that are not directly density-reachable from at least one core object are classified as:
a) Border points
b) Core points
c) Noise
d) Central points
**Correct Answer: c) Noise**
23. Which type of clustering algorithm explicitly builds a tree-like hierarchy of clusters?
a) Partitional algorithms
b) Density-based algorithms
c) Hierarchical algorithms
d) Model-based algorithms
**Correct Answer: c) Hierarchical algorithms**
24. If a k-means algorithm initializes its centroids randomly, what is a potential issue?
a) It will always converge faster.
b) It may lead to different clustering results on different runs.
c) It cannot handle large datasets.
d) It makes the algorithm more robust to outliers.
**Correct Answer: b) It may lead to different clustering results on different runs.**
25. In the context of clustering, what is "Nobjects"?
a) The number of clusters.
b) The total number of data points (observations).
c) The number of centroids.
d) The number of iterations.
**Correct Answer: b) The total number of data points (observations).**
26. Which statement is true regarding partitional clustering?
a) It always produces overlapping clusters.
b) It creates a hierarchical decomposition.
c) Each instance is placed in exactly one of K non-overlapping clusters.
d) It does not require the number of clusters to be specified.
**Correct Answer: c) Each instance is placed in exactly one of K non-overlapping clusters.**
27. The `dist(p,q)` in `NEps(p)` refers to:
a) The density of point p.
b) The similarity measure between points p and q.
c) The number of neighbors of p.
d) The cluster ID of point q.
**Correct Answer: b) The similarity measure between points p and q.**
28. What is a common characteristic of both k-means and k-NN?
a) Both are unsupervised learning algorithms.
b) Both are "lazy learners."
c) Both involve the concept of 'k' (neighbors/clusters).
d) Both can directly identify noise points.
**Correct Answer: c) Both involve the concept of 'k' (neighbors/clusters).**
29. The image in the handout for DBSCAN shows `MinPts = 5` and `Eps = 1 cm`. If a point has 4 points (including itself) within 1 cm radius, is it a core point?
a) Yes, because it has points within Eps.
b) Yes, because 4 is close to 5.
c) No, because it does not meet the `MinPts` condition (4 < 5).
d) It depends on other factors.
**Correct Answer: c) No, because it does not meet the `MinPts` condition (4 < 5).**
30. If you are given a dataset without any labels and your goal is to find natural groupings, which type of learning would you primarily use?
a) Supervised Learning
b) Regression
c) Classification
d) Unsupervised Learning
**Correct Answer: d) Unsupervised Learning**

---
```