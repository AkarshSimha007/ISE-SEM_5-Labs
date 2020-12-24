import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


blackF_df=pd.read_csv("BlackFriday.csv")

print(blackF_df.head(5))

blackF_df.drop(['User_ID',"Product_ID",'Stay_In_Current_City_Years'],axis=1,inplace=True)

print(blackF_df.head(5))

print("\n******Filtering Empty Values******\n")
blackF_df["City_Category"]=blackF_df["City_Category"].fillna("A")

print(blackF_df.head(5))

print("\n\nMapping City Values\n")
blackF_df["City_Category"]=blackF_df["City_Category"].map({'A':'Metro cities','B':'Small Towns','C':'Villages'})
print(blackF_df.head(10))


print("Renaming Columns")
blackF_df.rename(columns={"Product_Category_1":"Baseball_Caps","Product_Category_2":"Wine_Tumblers","Product_Category_3":"Pet_Raincoats"},inplace=True)
print(blackF_df.head(5))

print("\n\n Marital Status Mapping\n\n")
blackF_df["Marital_Status"]=blackF_df['Marital_Status'].map({0:'Unmarried',1:'Married'})
print(blackF_df.head(100))

print("\n\n****Data Visualization****\n\n")
print(pd.crosstab(blackF_df.Gender,blackF_df.Baseball_Caps))
print("\n\n\n")
print(pd.crosstab(blackF_df.Gender,blackF_df.Pet_Raincoats))


ax=sns.countplot(data=blackF_df,x="Gender",hue='Pet_Raincoats',palette='Set2')
ax.set(title="Male and Female who bought Pet Raincoats",xlabel='Gender',ylabel='Count')
plt.show()


print("\n\n*****Data visualization based on city category")

ax=sns.countplot(data=blackF_df,x="Gender",hue="City_Category",palette='Set3')
ax.set(title="Male and Female belonging to different cities",xlabel='Gender',ylabel='Count')
plt.show()