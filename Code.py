import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#define dataset
iris = pd.read_csv("iris.csv")
print(iris)
#create pairs plot for all numeric variables
sns.pairplot(iris)
plt.show()
sns.pairplot(iris[['sepal_length', 'sepal_width']])
plt.show()
sns.pairplot(iris, hue='species')
plt.show()
