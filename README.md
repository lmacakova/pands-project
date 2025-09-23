![iris](https://images.pexels.com/photos/31178524/pexels-photo-31178524.jpeg)

# Programming for Data Analytics – Project  
## Author: Lucia Macakova  

---

### About Project
This project is my submission for the module *Programming and Scripting*. It is an analysis of the classic [Iris dataset](https://en.wikipedia.org/wiki/Iris_flower_data_set). The notebook `iris_analysis.ipynb` contains the full analysis, explanations, plots, and results.

---

### Iris Dataset
The Iris dataset is a small but famous dataset used since 1936 to demonstrate classification techniques. It contains **150 samples** of three Iris species, each with **50 observations**:  

- *Iris setosa*  
- *Iris versicolor*  
- *Iris virginica*  

For each flower, four morphological features were measured:  

- Sepal length (cm)  
- Sepal width (cm)  
- Petal length (cm)  
- Petal width (cm)  

This dataset is often used as a benchmark for statistics and machine learning.

---

### Tasks
- Download and store the dataset for analysis.
- Research and summarize the Iris dataset. 
- Perform exploratory data analysis (EDA)  
- Apply statistical tests.  
- Train and evaluate classification models.  

---

### Solution 
First, I created the iris dataframe with the URL address of the archive of the University of California [^1], a list of column names, and saved it as a csv file.\
Then I loaded libraries and iris.csv for analysis in iris_analysis.ipynb. I made a short review and summary with commands df.info() and df.describe(). 
I made summaries of morphological values along with summaries for species and saved them into folder summaries. I made explanatory data analysis with histograms, scatterplot, and violin plots.\
In analysis, I used 3 models and tested the accuracy: Linear discriminant analysis[^2], Logistic regression[^3], and Decision Tree Classifier[^4].
First, I divided the dataset into dataframe x for morphological values and series y for categorical species values. I encoded series y to numerical values 0,1,2 for species. I divided dataframe x and series y in train, tests sets to test the accuracy of the classification method [^5].
  

### Results: 
- Logistic Regression and LDA achieved near-perfect accuracy.  
- Decision Tree was interpretable but less stable and slightly less accurate, confirming petals are the best predictors.  
- Confusion matrices showed most misclassifications occurred between *Versicolor* and *Virginica*.  

---

### How to Use
1. Clone this repository.  
2. Open `iris_analysis.ipynb` in Jupyter Notebook or JupyterLab.  
3. Run cells step by step to reproduce the analysis.  
4. Plots and summaries are saved automatically into the `summaries_variables/` and `plots/` folders.  

---

### Contact
Lucia Macakova\
📧 G00439449@atu.ie  

---

### Resources:
[^1]:   https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data
[^2]:   https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html     
[^3]:   https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression
[^4]:   https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html
[^5]:   https://www.w3schools.com/python/python_ml_train_test.asp 


