import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

# Display the first few rows
print("First few rows of the dataset:")
print(df.head())

# Explore the structure
print("\nData types and missing values:")
print(df.info())
print("\nMissing values in the dataset:")
print(df.isnull().sum())

# Since the Iris dataset has no missing values, no cleaning is required.
