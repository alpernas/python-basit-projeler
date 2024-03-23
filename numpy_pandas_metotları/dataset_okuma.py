import pandas as pd
import numpy as np
dataset=pd.read_csv("USvideos.csv")
newdataset=dataset.drop(["video_id","trending_date"],axis=1)
newdataset.to_csv("newvideo",index=False)
excelset=pd.read_excel("Book 1.xlsx")
excelset["colums5"]=["alper","emirhan","sinem","ahmet"]
excelset.to_excel("kitap.xlsx")