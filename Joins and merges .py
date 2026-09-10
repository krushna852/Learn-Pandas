import pandas as pd
import numpy as np

data ={
    "Name":["Krushna","Suraj","Mane","Krushna",np.nan,"Aniket"],
    "Age":[20,16,20,20,np.nan,18],
    "Department":["Ml Engineer","Data Scientist","Data Scientist","Ml Engineer",np.nan,"Production Manager"],
    "Salary":[7500000,5400000,6000000,7500000,np.nan,10000000]     
}


df1=pd.DataFrame(data)

data={
    "Department":["Ml Engineer","Data Scientist","Data Scientist","Ml Engineer",np.nan,"Production Manager"],
    "Maneger":["Kick","Staish","Carry","Ashish","Bhuham","Suram"],
    "Location":["Canada","India","India","Us","France","South Korea"]
}

df2=pd.DataFrame(data)

temp=pd.concat([df1,df2],axis=0)
print(temp)

df=pd.concat([df1,df2],axis=1)
print(df)

tem=pd.merge(df1,df2,on="Department")
print(tem) 