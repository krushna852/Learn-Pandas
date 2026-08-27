import pandas as pd

s1=pd.Series([562,33,25,88,60])

s1.name="Price"

name=["apple","Banana","Kerray","Pineapple","Grapes"]
s1.index=name
print(s1)

print(s1["Grapes"])
print(s1.iloc[3])

#labled Based Indexing : - loc

print(s1.loc["apple"])

print(s1.loc["apple":"Pineapple"]) # In Lable based Indexing staring and ending both included in o/p
#start (included) : End (Included) : step

print(s1.loc[["apple","Grapes","Pineapple"]])

#Craeting Series from Dict

pro={"apple":0.2,"Carraot":0.5,"Chicken":3,"Banana":0.6}
s2=[pd.Series(pro,name="Krushna")]
print(s2)