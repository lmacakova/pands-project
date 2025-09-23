import pandas as pd

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

# Naming the columns
col_names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]

# Creating csv file
iris = pd.read_csv(url, names=col_names)
iris.to_csv('iris.csv', index=False)
