import numpy as np
import pandas as pd
"""

df=pd.DataFrame([["bilişim",3000,"mustafa"],["insan kaynakları",3500,"jale"],["üretim",2500,"kadir"],["üretim",4500,"zeynep"],["bilişim",4000,"murat"],["insan kaynakları",2000,"ahmet"]],index=[0,1,2,3,4,5],columns=["departman","maaş","çalışan"])
df.index.names=["index"]
print(df)
print("-----")
depgrup=df.groupby("departman")
print(depgrup["maaş"].sum())
print(depgrup["maaş"].sum().loc[["bilişim"]])
print(depgrup.count())
print(depgrup.max())
print(df.groupby("departman").max()["maaş"].loc["bilişim"])

print(depgrup["maaş"].mean().loc["bilişim"])
"""

arr=np.array([["FRANCE","MBAMPE",12390],["GERMANY","NEUER",10200],["PORTEKİZ","C.RONALDO",25000],["FRANCE","BENZEMA",23000],["PORTEKİZ","NANİ",8000],["TÜRKEY","ARDA GÜLER",11000]])
df=pd.DataFrame(arr,columns=["ÜLKESİ","ADI","MAAŞ"])
print(df)
depgrup=df.groupby("ÜLKESİ")
print(depgrup["MAAŞ"].sum())
print("------")
print(depgrup["MAAŞ"].sum().loc["FRANCE"])
print("-------")
print(depgrup.count())
print("------")
print(depgrup["MAAŞ"].max())
