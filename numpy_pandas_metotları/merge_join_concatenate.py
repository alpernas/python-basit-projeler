import pandas as pd
import numpy as np
#concat metotu 2 dataframe'i alt alta yada yan yana birleştirme işlemi yapar
dataset1={"A":["A1","A2","A3","A4"],
          "B":["B1","B2","B3","B4"],
          "C":["C1","C2","C3","C4"]}
dataset2={"A":["A5","A6","A7","A8"],
          "B":["B5","B6","B7","B8"],
          "C":["C5","C6","C7","C8"]}
df1=pd.DataFrame(dataset1,index=[1,2,3,4])
df2=pd.DataFrame(dataset2,index=[5,6,7,8])
print(pd.concat([df1,df2],axis=0))
print("-----")
print(pd.concat([df1,df2],axis=1))

#join metotu 2 dataframe'i birleşleştirme işlemi yapar
dataset3={"A":["A1","A2","A3","A4"],
          "B":["B1","B2","B3","B4"]}

dataset4={"X":["X1","X2","X3"],
          "Y":["Y1","Y2","Y3"]}
df3=pd.DataFrame(dataset3)
df4=pd.DataFrame(dataset4)
print(df3.join(df4))
print(df4.join(df3))

#ortak anahtar keliğmesinin ortak k degerlerine göre yeni tablo oluşturuyor
dataset5={"A":["A1","A2","A3"],
          "B":["B1","B2","B3"],
          "anahtar":["k1","k2","k3"]}

dataset6={"X":["X1","X2","X3","X4"],
          "Y":["Y1","Y2","Y3","Y4"],
          "anahtar":["k1","k2","k5","k4"]}
df5=pd.DataFrame(dataset5)
df6=pd.DataFrame(dataset6)
print(pd.merge(df5,df6,on="anahtar"))