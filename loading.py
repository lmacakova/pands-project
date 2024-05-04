import pandas as pd

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

# Define the column names
col_names = ["sepal_length_in_cm", "sepal_width_in_cm", "petal_length_in_cm", "petal_width_in_cm", "species"]

# Read data from URL
iris = pd.read_csv(url, names=col_names)
iris.to_csv('iris.csv', index=False)


