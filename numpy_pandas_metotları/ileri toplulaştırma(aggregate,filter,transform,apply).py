import pandas as pd
import numpy as np
df=pd.DataFrame({'gruplar':['a','b','c','a','b','c'],
                 'degişken1':[10,23,33,22,11,99],
                 'degişken2':[100,253,333,262,111,969]},
                columns=["gruplar","degişken1","degişken2"])
print(df)
#aggregate
"""print(df.groupby('gruplar').mean())
print(df.groupby('gruplar').aggregate([min,np.median,max]))
print(df.groupby("gruplar").aggregate({"degişken1":min,"degişken2":max}))
"""
#filter
def filter_funk(x):
    return x["degişken1"].std()>9
print(df.groupby("gruplar").filter(filter_funk))

#transform
df.transform(lambda x:x-x.mea)