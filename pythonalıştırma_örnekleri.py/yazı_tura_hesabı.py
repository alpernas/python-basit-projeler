import random
yazı_sayısı=0
say_yazı=0
say_tura=0
while True:
    yazı_sayısı+=1
    yazı=random.randint(1,2)
    if yazı==1:
        print(f"{yazı_sayısı}. deneme yazı geldi")
        say_yazı+=1
    else:
        print(f"{yazı_sayısı}. deneme tura geldi")
        say_tura+=1
    if yazı_sayısı==10:
        print("toplam yazı sayısı:{}\ntoplam tura sayısı:{}".format(say_yazı,say_tura))
        break
