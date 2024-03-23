import pandas as pd
import numpy as np
"""dataset=pd.read_csv("mls-salaries-2017.csv")
print(dataset.columns)
#print(dataset.head(n=10))
#print(dataset[:10])
#print(len(dataset.index))
#print(dataset.index)
#print(dataset["base_salary"].mean())
#print(dataset["base_salary"].max())
#print(dataset[dataset["guaranteed_compensation"]==dataset["guaranteed_compensation"].max()]["last_name"])
# print(dataset[dataset["last_name"]=="Gonzalez Pirez"]["position"].iloc[0])
print(dataset.groupby("position")["base_salary"].mean())
print(dataset.groupby("position").nunique())
print(dataset["position"].value_counts())
print(dataset["club"].value_counts())

def soyad(soy):
    if "son" in soy.lower():
        return True
    return False
print(dataset[dataset["last_name"].apply(soyad)])
"""
dataset=pd.read_csv("mls-salaries-2017.csv")
print(dataset.head(10))
print(dataset.info())
print(dataset.index)
print(len(dataset.index))
print(dataset["base_salary"].mean())
print(dataset[dataset["guaranteed_compensation"].max()==dataset["guaranteed_compensation"]])
print("-------")
print(dataset[dataset["last_name"]=="Gonzalez Pirez"]["position"])
print("-------")
soccergrup=dataset.groupby(["position"])
print(soccergrup["base_salary"].mean().loc[["D","M"]])
print(dataset["position"].nunique())
print(dataset["position"].value_counts())
print(dataset["club"].value_counts())
print("-----------")
def soyad(soy):
    return soy.lower() in "son"
print(dataset[dataset["last_name"].apply(soyad)])