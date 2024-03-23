liste1=[1,2,3,4,5]
liste2=[]
for i in liste1:
    liste2.append(i)
print(liste2)

liste3=[x for x in liste1]
print(liste3)

liste4=[]
for i in liste1:
    liste4.append(i*2)
print(liste4)

liste5=[i*2 for i in liste1]
print(liste5)

liste6=[(1,2),(3,4),(5,6)]

liste7=list()
for i,j in liste6:
    liste7.append(i*j)

print(liste7)
liste8=[i*j for i,j in liste6]
print(liste8)

s="python"
liste9=[]
for i in s:
    liste9.append(3*i)
print(liste9)

liste10=[i*3 for i in s]
print(liste10)

liste=[[1,2,3,4],[5,6,7,8],[9,10]]
liste2=[]
for i in liste:
    for j in i:
      liste2.append(j)
print(liste2)
liste3=[j for i in liste for j in i]
print(liste3)