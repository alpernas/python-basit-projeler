sayı=int(input("sayı giriniz:"))
top=0
for i in range(1,sayı):
    if sayı%i==0:
        top+=i
if sayı==top:
    print("sayınız mükemmel sayıdır")
else:print("sayınız mükemmel sayı degildir")
