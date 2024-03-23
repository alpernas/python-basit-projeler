import numpy as np
import pandas as pd
m=np.random.randint(1,30,size=(10,3))
df=pd.DataFrame(m,columns=["var1","var2","var3"])
print(df)
print(df.loc[0:3])
print("------")
print(df.iloc[:3,1:2])
print(df.loc[:3])
print(df[["var2"]])
print(df["var1"].loc[6])
