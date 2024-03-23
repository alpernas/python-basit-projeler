sayı=input("sayı giriniz:")
top=0
geçici=int(sayı)
kalan=0
while geçici>0:
    kalan=geçici%10
    top+=kalan**len(sayı)
    geçici=geçici//10
if top==int(sayı):
    print("armsterg sayıdır")
else:
    print("armstorng sayı degildir")