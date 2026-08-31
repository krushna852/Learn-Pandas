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
print(df,"\n")

print(df.head(1),"\n")

print(df.tail(1))
