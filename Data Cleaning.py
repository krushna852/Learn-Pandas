import pandas as pd 
import numpy as np


data ={
    "Name":["Krushna","Suraj","Mane","Garudkar",np.nan,"Aniket"],
    "Age":[20,16,20,23,np.nan,18],
    "Department":["Ml Engineer","Data Scientist","Data Scientist","Manager",np.nan,"Production Manager"],
    "Salary":[7500000,5400000,6000000,5300000,np.nan,10000000]     
}

df=pd.DataFrame(data)

#Data Cleaning:-

print(df)

df["Promoted Slaray"] = (df["Salary"]*0.2) + df["Salary"]
print(df.isnull().sum())

#Remark:- Dealing With Missing Values

#method 1 :- removes the null values
print(df.dropna())

#how = "any":-

print(df.dropna(how="any")) #any row that have a any null value

# how = "all":-

print(df.dropna(how="all")) #Drop a row only if all values in row is null


#method:- fill the null values
#df.fillna()

#Passing single argument all missing values fill with argument
print(df.fillna(10))

#Repalce with mean
temp=df["Age"].fillna(df["Age"].mean())
print(temp)

#replace Salary with median
temp=df["Salary"].fillna(df["Salary"].median())
print(temp)

#Remark :- There are also 2 more method to fill missing values 

#Forward fill

print(df.ffill())  # Fill missing Value with last known value

#Backward Fil

print(df.bfill()) #Fill missing values with last Known Value


#Repalce any value

print(df["Name"].replace("Mane","Krushna"))