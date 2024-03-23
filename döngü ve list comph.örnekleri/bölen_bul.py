for i in range(1,100):
    if i%3!=0:
        continue
    else:print(i)

print("**********")
liste=[i for i in range(1,100) if i%3==0]
print(liste)