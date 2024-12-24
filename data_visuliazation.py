# Line chart showing trends over time (using sepal length for illustration)
from lib2to3.pgen2.pgen import DFAState


plt.figure(figsize=(10, 6))
plt.plot(DFAState.index, df['sepal length (cm)'])
plt.title('Line Chart of Sepal Length Over Samples')
plt.xlabel('Sample Index')
plt.ylabel('Sepal Length (cm)')
plt.show()

# Bar chart showing the comparison of average petal length per species
plt.figure(figsize=(10, 6))
grouped['petal length (cm)'].plot(kind='bar', color='skyblue')
plt.title('Average Petal Length per Species')
plt.xlabel('Species')
plt.ylabel('Average Petal Length (cm)')
plt.xticks(rotation=0)
plt.show()

# Histogram of a numerical column (sepal length)
plt.figure(figsize=(10, 6))
plt.hist(df['sepal length (cm)'], bins=20, color='green')
plt.title('Histogram of Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.show()

# Scatter plot to visualize the relationship between sepal length and petal length
plt.figure(figsize=(10, 6))
plt.scatter(df['sepal length (cm)'], df['petal length (cm)'], c='blue', marker='o')
plt.title('Scatter Plot of Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.show()
