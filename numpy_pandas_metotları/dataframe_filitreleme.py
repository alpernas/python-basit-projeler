import numpy as np
import pandas as pd
from numpy.random import randn

df=pd.DataFrame(randn(3,3),index=["A","B","C"],columns=["ev","araba","arsa"])
print(df>-1)
print(df[df>0])

print(df)
print(df[df["araba"]<0])

print(df[(df["ev"]>0) & (df["araba"]>0)])

df["dükkan"]=pd.Series(randn(3),index=["A","B","C"])

df["tarla"]=["newa","newb","newc"]
df["bakkal"]=[12,56,37]
print(df)

df.set_index("tarla",inplace=True)
print(df)
