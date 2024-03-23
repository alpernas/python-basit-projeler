print("""
****************
Atm Makinesine Hoşgeldiniz.

işlemler:

1.bakiye sorgulama:
2.para yatırma:
3.para çekme
4.para transferi

kartınızı geri almak  için 'q' ya basınız..

***************
""")
bakiye=1200
while True:
    işlem=input("yapmak istediğiniz işelmi seçiniz:")
    if işlem=='q':
        print("kartınızı alınız..")
        break
    elif işlem=="1":
        print("bakiyeniz:",bakiye)

    elif işlem=="2":
        yatır=int(input("lütfen yatırmak istediğiniz tutarı giriniz: "))
        bakiye+=yatır
    elif işlem=="3":
        çekme=int(input("çekmek istediğiniz para"))
        if çekme>bakiye:
            print("bakiyeniz yetersiz")
        else:
            bakiye-=çekme
    elif işlem=="4":

        iban=(input("ibanı giriniz:"))
        if len(iban)!=24:
            print("geçrsiz iban giriniz:")
        else:
            gönder=int(input("gendermek istediğiniz tutar:"))
            if gönder>bakiye:
                print("bakiyeniz yetersiz işelminiz gerçekleştirilmedi..")
            else:bakiye-=gönder

