import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

titanic_df=pd.read_csv('titanictrain.csv')
titanic_df['Survived']=titanic_df['Survived'].map({0:'Died',1:'Survived'})

print(titanic_df.head(5))

print("\n\n***DATA TRANSFORMATION***\n\n")

titanic_df.drop(['Parch','PassengerId','Name','Ticket'],axis=1,inplace=True)
print("Data headers after Dropping columns\n")
print(titanic_df.head(5))
titanic_df.drop(['SibSp','Fare'],axis=1,inplace=True)
print("\nData headers after Dropping some more columns\n")
print(titanic_df.head(5))

print("\n\n********\n\n")

titanic_df['Pclass']=titanic_df['Pclass'].map({1:'Luxury Class',2:'Economy Class',3:'Lower Class'})
print(titanic_df.head(5))


titanic_df['Embarked']=titanic_df['Embarked'].fillna('S')
print("\n======Data Headers After Filling with default value for Embarked Column =======")
print("\n")
print(titanic_df.head(5))
print("\n")

print("\n Data Visualizations \n")
print("Viz.1: Survival rate based on passenger Sitting class")
ax=sns.countplot(x='Pclass',hue='Survived',palette='Set1',data=titanic_df)
ax.set(title='Passenger status(S/D) against Passenger Class',xlabel='Passenger Label',ylabel='Total')
plt.show()

print("Viz.2: Survival Rate Based on Gender")
print(pd.crosstab(titanic_df["Sex"],titanic_df.Survived))
ax = sns.countplot(x = 'Sex', hue = 'Survived', palette = 'Set2', data = titanic_df)
ax.set(title = 'Total Survivors According to Sex', xlabel = 'Sex', ylabel='Total')
plt.show()

print("Viz.3: Survival Rate based on Age")
interval=(0,18,35,60,120)
categories=['Children','Teen','Adult','Old']
titanic_df['Age_cats']=pd.cut(titanic_df.Age,interval,labels=categories)
ax=sns.countplot(x='Age_cats',hue='Survived',palette='Set3',data=titanic_df)
ax.set(xlabel='Age Categories',ylabel='Total',title="Age Categorical Survival Distribution")
plt.show()

print("Viz.4:Survival rate based on passenger Embarked Port")
print(pd.crosstab(titanic_df['Embarked'],titanic_df.Survived))
ax=sns.countplot(x='Embarked',hue='Survived',palette='Set1',data=titanic_df)
ax.set(title='Survival distribution according to Embarking Port')
plt.show()
