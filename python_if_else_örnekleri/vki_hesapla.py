#kullanıcıdan alınan boy kilo degerlerine göre beden kitle indeksi

boy=float(input("boyunuzu giriniz:"))
kilo=int(input("kilonuzu giriniz:"))
vki=kilo/(boy*boy)
if vki<18.5:
    print("zayıfsınız vki:",vki)
elif vki>=18.5 and vki<25:
    print("normalsiniz vki:",vki)
elif vki>=25 and vki<30:
    print("fazla kilolusunuz vki:",vki)
elif vki>=30:
    print("obezsiniz vki:",vki)
