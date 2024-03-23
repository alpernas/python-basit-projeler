import pandas as pd
import numpy as np
df=pd.DataFrame({"A":[1,2,3,4,5,6],
                 "B":[100,100,200,300,300,100],
                 "C":["alper","mustafa","dogan","zeynep","ali","murat"]})

print(df.head())
print("-----")
print(df["B"].unique())
print(df["B"].describe())
print(df[df["B"]>100].value_counts())
print(df[(df["A"]>=4) & (df["B"]==300)])

def times3(x):
    return x*3
print(df["B"].apply(times3))
df["B"]=df["B"].apply(lambda x:x*3)
print(df)
print(df["C"].apply(len))
df.drop("C",axis=1,inplace=True)
#print(df.columns)
#print(len(df.index))
#print(len(df.columns))
#print(df.columns.name)
#print(df.sort_values("B",ascending=False))

df1=pd.DataFrame({"ay":["mart","nisan","mayıs","mart","nisan","mayıs","mart","nisan","mayıs"],
                  "şehir":["ankara","ankara","ankara","kelkit","kelkit","kelkit","erzincan","erzincan","erzincan"],
                  "nem":[10,25,50,21,29,45,24,89,67]})
print(df1)
print("------")
print(df1.pivot_table(index="ay",columns="şehir",values="nem"))
print(df1.pivot_table(index="şehir",columns="ay",values="nem"))

