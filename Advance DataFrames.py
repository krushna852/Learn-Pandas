import pandas as pd
import numpy as np


data ={
    "Name":["Krushna","Suraj","Mane","Garudkar","Magar","Aniket"],
    "Age":[20,16,20,23,24,18],
    "Department":["Ml Engineer","Data Scientist","Data Scientist","Manager","Manager","Production Manager"],
    "Salary":[7500000,5400000,6000000,5300000,np.nan,10000000]     
}

df=pd.DataFrame(data)
print(df.info())

#Broadcasting :- Here 1D Ds is Multiply By The Scalar

df["Salary"] = df["Salary"] + 50000
print(df["Salary"])

#Columns also Known as Features

#Renaming Columns :- 

df.rename(columns={"Department":"Dept"},inplace=True)
print(df) 

#Checked Unique Values in particular Column

print(df["Dept"].unique())

#Checked How many People Are Join in Each Department

print(df["Dept"].value_counts())

#Adding New Column

df["Promoted salary"] = (df["Salary"] * 0.1) + df["Salary"]
print(df)