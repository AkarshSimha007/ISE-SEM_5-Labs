import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df=pd.read_csv("StudentsPerformance.csv")
print(df.describe())
print()
print(df.info())
print()
print(df.head())
print()

df.drop(['lunch'],axis=1,inplace=True)
df['parental level of education']=df['parental level of education'].fillna("Not appliable")
print("*****")
print(df.head())
print("****************************")
print("Data Visualization")

ax = sns.countplot(x="test preparation course",hue='gender',palette='Set3',data=df)
ax.set(title="Course completion based on gender",xlabel="Course",ylabel="Total")
plt.show()

ax=sns.countplot(x="race/ethnicity",hue="gender",palette="Set2",data=df)
ax.set(title="Students belonging to each group based on Gender",xlabel="Groups",ylabel="Total")
plt.show()

interval=(0,40,50,75,100)
categories=['Fail','2nd Class','1st Class','Distinction']
df["mark_cats"]=pd.cut(df.mathscore,interval,labels=categories)

ax=sns.countplot(x="mark_cats",hue="gender",palette="Set2",data=df)
ax.set(title="Marks categories in math",xlabel="Categories",ylabel="No. of Students")
plt.show()