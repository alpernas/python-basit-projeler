import numpy as np
import pandas as pd
from numpy.random import randn

outerindex=["grup1","grup1","grup1","grup2","grup2","grup2","grup3","grup3","grup3"]
inerindex=["index1","index2","index3","index1","index2","index3","index1","index2","index3"]
hierarcy=list(zip(outerindex,inerindex))
hierarcy=pd.MultiIndex.from_tuples(hierarcy)
df=pd.DataFrame(randn(9,3),index=hierarcy,columns=["A","B","C"])
print(df)

print(df[["A"]])
print(df[["A"]].loc["grup1","index1"])
print(df.loc[["grup1","grup3"]])
print(df.loc["grup1"].loc[["index1","index2"]])
print(df["A"].loc["grup3"].loc[["index1"]])

df.index.names=["grups","indexes"]
print(df.loc["grup1"])
print(df.xs("grup1").xs("index1").xs("A"))
print(df.xs("index1",level="indexes"))

outerindex=["sınıf1","sınıf1","sınıf1","sınıf2","sınıf2","sınıf2","sınıf3","sınıf3","sınıf3"]
innerindex=["alper","melisa","sevgi","mahmut","ali","veli","kenan","kemal","sinem"]
hierarcy=list(zip(outerindex,innerindex))
hierarcy=pd.MultiIndex.from_tuples(hierarcy)
df=pd.DataFrame(data=randn(9,3),index=hierarcy,columns=["vize","final","büt"])
print(df.loc[["sınıf1"]].sum())
print("------")
print(df.loc[["sınıf3"]].mean())
print("------")
print(df[["vize","final"]].loc[["sınıf1","sınıf2"]])
print("------")

print(df[["büt"]].loc["sınıf1"].loc[["alper"]])
print("------")

df.index.names=["sınıflar","ögrenciler"]
print(df.xs("sınıf1").xs("alper").xs("vize"))
print("------")

print(df.xs("alper",level="ögrenciler"))
