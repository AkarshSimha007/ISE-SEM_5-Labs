import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

titanic_df=pd.read_csv("titanictrain.csv")
print(titanic_df.head(5))

print(titanic_df.describe)

titanic_df.drop(['Parch','PassengerId','Name','Ticket'],axis=1,inplace=True)

titanic_df['Survived']=titanic_df['Survived'].map({
    0:"Died",
    1:"Survived"
})

titanic_df['Pclass']=titanic_df['Pclass'].map({
    1:"Luxury Class",
    2:"Economy Class",
    3:"Lower Class"
})

titanic_df['Embarked']=titanic_df['Embarked'].fillna("S")

titanic_df['Embarked']=titanic_df['Embarked'].map({
    "C":"Cherbourg",
    "S":"Southampton",
    "Q":"Queenstown"
})
print(titanic_df.head(5))

print("**********Data Visualizations****************")

ax=sns.countplot(x='Pclass',hue='Survived',palette='Set1',data=titanic_df)
ax.set(title="Survival based on Passenger class",xlabel="Passenger Class",ylabel="Total")
plt.show()

print("Visualization #2 : Survival Rate Based on Gender")
print(pd.crosstab(titanic_df["Sex"],titanic_df.Survived))

ax=sns.countplot(data=titanic_df,x="Sex",hue="Survived",palette="Set2")
ax.set(title="Survival based on gender",xlabel="Sex",ylabel="Total")
plt.show()

print("Visualization #3 : Survival Rate Based on Passenger Age Group")
interval=(0,18,35,60,120)
categories=['Children','Teens','Adult','Old']

titanic_df["Age_Cats"]=pd.cut(titanic_df.Age,interval,labels=categories)

ax=sns.countplot(x="Age_Cats",hue="Survived",palette="Set3",data=titanic_df)
ax.set(title="Survival based on age category",xlabel="Age Category",ylabel="Total")
plt.show()