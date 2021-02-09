import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv("iris.csv")

print(df.describe)
print(df.head())

df.drop(['Sepal_Length'],inplace=True,axis=1)


print(df.groupby('Class').agg(['mean']))

ax = sns.countplot(data = df,hue = 'Class',palette="Set1",x = ' Sepal_Width')
ax.set(title="Flowers of each specie",xlabel="Sepal Width",ylabel="No.of Flowers")
plt.show()

interval = (0,1,2,4)
category = ['<1','1 to 2','>2']
df['Petal_Catg'] = pd.cut(df[' Petal_Width'],interval,labels=category)
ax = sns.countplot(data = df,x = 'Petal_Catg',hue='Class',palette='YlOrRd')
ax.set(title='Petal Width',xlabel='Category of Petals',ylabel='No. of flowers')
plt.show()

ax = sns.countplot(data = df[df['Class'] != 'Iris-setosa'],hue = 'Class', x = ' Sepal_Width',palette='Set1')
ax.set(xlabel='Sepal Width',ylabel='No. of flowers')
plt.show()

print(pd.crosstab(df["Class"],df[" Sepal_Width"]))