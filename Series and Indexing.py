import pandas as pd


s1=pd.Series([10,20,30,40,50])  # it is 1D data structure and it is homogenous (only one data type)
print(s1)

print(s1.dtype)


s2=pd.Series([10,63, 45,2.3])
print(s2,"\n",s2.dtype)

s3=pd.Series(["krushna",56.2,56,1])
print(s3,"\n",s3.dtype)

print(s3.values)

print(s1.index)

s3.name="Random"
print(s3)  

#Indexing

print(s3[0])
print(s3[1])

print(s2[::2]) #slicing start : stop (exlcuded) : step

#Location based Indexing

print(s1.iloc[2])

#for Multiple Index

print(s2.iloc[[0,2,1]])
