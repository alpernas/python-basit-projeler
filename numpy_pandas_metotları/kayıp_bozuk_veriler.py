import numpy as np
import pandas as pd


arr=np.array([[12,45,np.nan],[5,np.nan,21],[67,np.nan,np.nan]])
df=pd.DataFrame(data=arr,index=['A','B','C'],columns=["colums1","colums2","colums3"])
#df.dropna(axis=1,inplace=True)
df.dropna(thresh=2,axis=0,inplace=True)
print(df)

#df.fillna(value=1, inplace=True)
#print(df.loc['A'].sum())
#print(df.sum().sum())
#print(df.size)
#print(df.isnull().sum())
"""
def calculateMean(df):
    totalsum=df.sum().sum()
    totalnum=df.size-df.isnull().sum().sum()
    return totalsum/totalnum
df.fillna(value=calculateMean(df),inplace=True)
print(df)

arr=np.array([[12,np.nan,56],[32,np.nan,np.nan],[21,90,np.nan]])
df=pd.DataFrame(arr,index=['A','B','C'],columns=["colums1","colums2","colums3"])
print(df)
#df.dropna(axis=1,inplace=True)
#df.dropna(axis=0,inplace=True)
#df.dropna(thresh=3,axis=1,inplace=True)
#df.fillna(value=1, inplace=True)
print(df['colums2'].sum())
print(df.loc["A"].sum())
print(df.sum().sum())
print(df.size)
print(df.isna().sum())
"""