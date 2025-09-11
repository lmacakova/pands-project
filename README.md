![iris](https://images.pexels.com/photos/31178524/pexels-photo-31178524.jpeg)
)
# Programing for Data Analytics - Project
## Author: Lucia Macakova
## Data Analyses of Iris Dataset
### About
I am a student of the [Atlantic Technical University](https://www.atu.ie/) in the program [Higher Diplomma in Science and Data Analytics](https://www.gmit.ie/higher-diploma-in-science-in-computing-in-data-analytics). This project is my project for the module Programming and Scripting.

### Iris Dataset
The Iris flower dataset is a collection of morphological measurements of 150 iris plants used in 1936 by statistician and biologist [Ronald Fischer](https://en.wikipedia.org/wiki/Ronald_Fisher) as an example of [linear dicriminant analysis](https://en.wikipedia.org/wiki/Linear_discriminant_analysis). Data were collected by botanist [Edgar Anderson](https://en.wikipedia.org/wiki/Edgar_Anderson).Dataset consists of 3 species of genus (*Iris*), [Bristle-Pointed Iris](https://en.wikipedia.org/wiki/Iris_setosa#:~:text=Iris%20setosa%2C%20the%20bristle%2Dpointed,Limniris%20and%20the%20series%20Tripetalae.) (*Iris Setosa*), [Virginia Blueflag Iris](https://en.wikipedia.org/wiki/Iris_virginica) (*Iris Virginica*), and [Blue Flag Iris](https://en.wikipedia.org/wiki/Iris_versicolor) (*Iris Versicolor*), everyone is represented with 50 samples. In each sample, four features of the flower were measured: Sepal length in cm, sepal width in cm, petal length in cm, and petal width in cm. Over the years, the Iris dataset became a typical test case for many statistical classification techniques in machine learning [^1].

### Tasks:

-   To research the data set online  and write a summary about it.
-   To download the data set and add it to your repository. 
-   To write a program that: 
    -   Outputs a summary of each    variable to a single text file
    -   To save a histogram of each variable to png files
    -   Outputs a scatter plot of each pair of variables
-   To perform any other analysis that could be considered appropriate

### Solution:

#### Researching and describing the dataset
First, I created the iris dataframe with the URL address of the archive of the University of California [^2], a list of column names, and saved it as a csv file. Then I loaded libraries and iris.csv for analysis in iris_analysis.ipynb. Short review and summary with commands df.info() and df.describe(). 
I made summaries of 4 variables of morphological values and saved them into folder summaries_variables. I made histograms of morphological values and saved them to the folder histograms_variables. "A histogram is a visualization tool that represents the distribution of one or more variables by counting the number of observations which fall within discrete bins." [^3]. Kernel density estimation lines help with the readability of histograms. 
Then I made scatterplot matrixes of morphological variables. Scatterplot is a plot where each record in a dataset is represented by a dot and the position of this dot represents values of the record for 2 variables, which can show us the correlation between variables and clustering of values into clusters [^4].
For better understanding of correlation between variables, I made a correlation matrix of morphological values with the use of the Pearson correlation coefficient [^5], with values above 0.59 to be considered as a "solid" correlation [^6].

#### Analysis
The aim of this dataset is to test various mathematical models to sort records with 4 attributes properly. I used 3 models and tested the accuracy: [Linear discriminant analysis](https://www.youtube.com/watch?v=azXCzI57Yfc), [Logistic regression](https://www.youtube.com/watch?v=yIYKR4sgzI8), and [Decision Tree Classifier](https://www.youtube.com/watch?v=_L39rN6gz7Y).
First, I divided the dataset into dataframe x for morphological values and series y for categorical species values. I encoded series y to numerical values 0,1,2 for species [^7]. I divided dataframe x and series y in train, tests sets to test the accuracy of the classification method [^8].
The dendrogram of dataframe x stays aside as an experiment: Just an interesting view of visible clusters in the dataframe. The records were not sorted into clusters [^9].
For classifications, I used classifiers from sklearn library LinearDescriminantAnalysis()[^10], LogisticRegression()[^11],DecisionTreeClassifier [^12], fitted them to train_x, train_y to create models and counted the score with train_x, train_y.

### How users can get started with the project
With README.md and then follow the steps in iris_analysis.ipynb.

### Contact:
Lucia Macakova\
email: G00439449@atu.ie

### Resources
[^1]: https://en.wikipedia.org/wiki/Iris_flower_data_set
[^2]: https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data
[^3]: https://seaborn.pydata.org/generated/seaborn.histplot.html
[^4]: https://www.w3schools.com/python/python_ml_scatterplot.asp
[^5]: https://en.wikipedia.org/wiki/Pearson_correlation_coefficient
[^6]: https://www.w3schools.com/datascience/ds_stat_correlation_matrix.asp
[^7]: https://scikit-learn.org/dev/modules/generated/sklearn.preprocessing. LabelEncoder.html
[^8]: https://www.w3schools.com/python/python_ml_train_test.asp
[^9]: https://seaborn.pydata.org/generated/seaborn.clustermap
[^10]:https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html
[^11]:https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression
[^12]:https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html




