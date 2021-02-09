import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 

bf_df=pd.read_csv("BlackFriday.csv")
print(bf_df.head())
print(bf_df.describe())

bf_df.drop(['User_ID','Product_ID','Stay_In_Current_City_Years'],axis=1,inplace=True)
print("***Filling Empty Values***")

bf_df["City_Category"]=bf_df["City_Category"].fillna("A")
print(bf_df.head())

bf_df["City_category"]=bf_df["City_Category"].map({
    "A":"Metro cities",
    "B":"Towns",
    "C":"Villages"
})

print(bf_df.head())

ax=sns.countplot(x='Gender',hue='Product_Category_1',palette='Set1',data=bf_df)
ax.set(title="Gender wise purchase",xlabel="gender",ylabel="Total")
plt.show()

# ax=sns.countplot(x="City_category",hue="Gender",palette="Set2",data=bf_df)
# ax.set(title="Gender based City category",xlabel="City",ylabel="Genders")
# plt.show()

ax = sns.countplot(data=bf_df,hue='Gender',x='City_Category',palette='Set1')
ax.set(title='Male and Female belonging to each city',xlabel='Gender',ylabel='Count')
plt.show()
