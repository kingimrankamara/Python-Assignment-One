# Compute basic statistics
from lib2to3.pgen2.pgen import DFAState


print("\nBasic statistics of the numerical columns:")
print(DFAState.describe())

# Perform groupings
grouped = df.groupby('species').mean()
print("\nMean of numerical columns grouped by species:")
print(grouped)

# Identify patterns
print("\nObservations:")
print("1. Setosa species has the smallest petal length and width.")
print("2. Virginica species has the largest petal length and width.")
print("3. Versicolor species falls between Setosa and Virginica in terms of petal dimensions.")
