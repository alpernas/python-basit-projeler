import pandas as pd
import numpy as np
m=np.random.randint(1,30,size=(10,3))
df=pd.DataFrame(m,columns=["var1","var2","var3"])
print(df)
print(df[["var1","var2"]][0:5])
print(df>4)
print("-------")
print(df[df["var2"]>23])
