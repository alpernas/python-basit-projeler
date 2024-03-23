import pandas as pd
import numpy as np
"""
m=np.random.randint(1,30,size=(5,3))
df=pd.DataFrame(m,columns=["var1","var2","var3"])
print(df)
df2=df+45
print(pd.concat([df,df2],ignore_index=True,axis=1))
df2.columns=["var1","var2","deg3"]
print(pd.concat([df,df2],ignore_index=True,join="inner"))
"""

#ileri birleştirme
df1=pd.DataFrame({'çalışanlar':["ali","veli","ayşe","fatma"],
                  'grup':["muhasebe","mühendislik","mühendislik","İK"]})
df2=pd.DataFrame({'çalışanlar':["ali","veli","ayşe","fatma"],
                  'ilk_giriş':[2010,2009,2014,2019]})

print(pd.merge(df1,df2))
print(pd.merge(df1,df2,on="çalışanlar"))
#çoktan teke
df3=pd.merge(df1,df2)
print(df3)
df4=pd.DataFrame({'grup':["muhasebe","mühendislik","İK"],
                  'müdür':["caner","mustafa","alper"]})
print(df4)

print(pd.merge(df3,df4))

#çoktan çoğa
df5=pd.DataFrame({'grup':["muhasebe","muhasebe","mühendislik","mühendislik","İK","İK"],
                  'yetenekler':["matematik","excel","kodlama","linux","excel","yönetim"]})
print(pd.merge(df5,df1))