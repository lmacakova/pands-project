# pands-project
## Author: Lucia Macakova
## Data Analyses of Iris Dataset
### About the Author
My name is Lucia Macakova and I am a student of the [Atlantic Technical University](https://www.atu.ie/) in the program [Higher Diplomma in Science and Data Analytics](https://www.gmit.ie/higher-diploma-in-science-in-computing-in-data-analytics). I am the only contributor to this project as this is my project for the module Programming and Scripting.

### Iris Dataset
The Iris flower dataset is a collection of morphological measurements of 150 iris plants used in 1936 by statistician and biologist [Ronald Fischer](https://en.wikipedia.org/wiki/Ronald_Fisher) as an example of [linear dicriminant analysis](https://en.wikipedia.org/wiki/Linear_discriminant_analysis). Data were collected by botanist [Edgar Anderson](https://en.wikipedia.org/wiki/Edgar_Anderson).Dataset consists of 3 species of genus (*Iris*), [Bristle-Pointed Iris](https://en.wikipedia.org/wiki/Iris_setosa#:~:text=Iris%20setosa%2C%20the%20bristle%2Dpointed,Limniris%20and%20the%20series%20Tripetalae.) (*Iris Setosa*), [Virginia Blueflag Iris](https://en.wikipedia.org/wiki/Iris_virginica) (*Iris Virginica*), and [Blue Flag Iris](https://en.wikipedia.org/wiki/Iris_versicolor) (*Iris Versicolor*), everyone is represented with 50 samples. In each sample, four features of the flower were measured: Sepal length in cm, sepal width in cm, petal length in cm, and petal width in cm. Over the years, the Iris dataset became a typical test case for many statistical classification techniques in machine learning [^1].

### Tasks:
 1. To research the data set online and write a summary about it.
 2. To fownload the data set and add it to your repository. 
 3. To write a program that:  
    - Outputs a summary of each variable to a single text file
    - Saves a histogram of each variable to png files
    - Outputs a scatter plot of each pair of variables
 4. To performs any other analysis that could be considered appropriate

### Solution:

#### Researching and describing dataset
First, I created iris dataframe with URL adress of archive of University of California [^2], list of column names and saved it as csv file. Then I loaded libraries and iris.csv for analysis in iris_analysis.ipynb. Short review and summary with command df.info() and df.describe(). 
I made summaries of 4 variables of morphological values and saved them into folder summaries_variables. I made histograms of morphological values and saved them to folder histograms_variables. "A histogram is a visualization tool that represents the distribution of one or more variables by counting the number of observations which fall within discrete bins." [^3]. Kernel density estimation lines help with readability of histograms. 
Then I made scatterplot matrixes of morphological variables. Scatterplot is plot where each record in dataset is represented by dot and position of this dot represents values of record for 2 variables, which can show us correlation between variables and clustering of values into clusters [^4].
For better understanding of correlation between variables I made correlation matrix of morphological values with use of pearson correlation coefficient [^5], where values above 0.59 can be considered as "solid" correlation [^6].

#### Analysis
Aim of this dataset is to test various matematical models to properly sorted records just with 4 atributs. I used 3 models and test the accuracy: [Linear discriminant analysis](https://www.youtube.com/watch?v=azXCzI57Yfc), [Logistic regression](https://www.youtube.com/watch?v=yIYKR4sgzI8), and [Decision Tree Classifier](https://www.youtube.com/watch?v=_L39rN6gz7Y).
First, I divided dataset into dataframe x for morphological values and series y for categorical values of species. I encoded series y to numerical values 0,1,2 for species [^7]. I divide dataframe x and series y in train, tests sets to test accuracy of classification method [^8].
Dendrogram of dataframe x stays aside as an expriment: Just interesting view of visible clusters in dataframe. The records were not sorted into clusters [^9]. 


### How users can get started with the project
With README.md and then follow the steps in iris_analysis.ipynb.

### Contact:
Lucia Macakova

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




