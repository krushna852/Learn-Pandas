import pandas as pd
import numpy as np

#DataFrames:- It is a 2D data structure

#Craeting From Dict:-

data ={
    "Name":["Krushna","Suraj","Mane","Garudkar","Magar","Aniket"],
    "Age":[20,16,20,23,24,18],
    "Department":["Ml Engineer","Data Scientist","Data Analysis","DevOPS","Manager","Production Manager"],
    "Salary":[7500000,5400000,6000000,5300000,np.nan,10000000]     
}

df=pd.DataFrame(data)
#print(df,"\n")

#print(df.head(1),"\n")

print(df.tail(3))

#loc and iloc :-

#iloc() :-
print(df.iloc[[1,3,2]])
print(df.iloc[0:4])  # start (include) : stop (exclude) : step

#loc() :-

print(df.loc[1:3]) # start (include) : stop (include): step

#note if we want specific rows and specific columns

print(df.loc[0:3,["Department","Salary"]])

print(df.iloc[1:3,:3])

#Accesed Particular Column
print(df["Department"])

#Multiple Columns
print(df[["Age","Name"]])

#Deletion

#1. Column (axis=1):-

temp=df.drop("Department",axis=1)
df.drop("Department",axis=1) # Not change in orignal dataframe
print(df)
print(temp)
df.drop("Department",axis=1,inplace=True) #Now Orignal Dataframe changes
print(df)


#2.Row(axis=0):-

temp=df.drop(3,axis=0)
print(temp)


#Some Imp functions: 

print(df.shape) #Indexes Column are not counted as column
