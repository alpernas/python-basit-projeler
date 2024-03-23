print("""**************

Hesap makinası programı

İşlemler:

1.Toplama işlemi:
2.Çıkarma işlemi:
3.Çarma işlemi:
4.Bölme işlemi
********************
""")
işlem=input("işlem giriniz:")
sayı=int(input("1 sayı:"))
sayı1=int(input("2. sayı:"))

if işlem=="1":
    print("{} ile {} in toplamı:{}".format(sayı,sayı1,sayı1+sayı) )
elif işlem=="2":
    print("{} ile {} in farkı:{}".format(sayı,sayı1,sayı1-sayı) )
elif işlem=="3":
    print("{} ile {} in çarpımı:{}".format(sayı,sayı1,sayı1*sayı) )
elif işlem=="4":
    print("{} ile {} in bölümü:{}".format(sayı,sayı1,sayı1/sayı) )
else:
    print("geçersiz işelm girdiniz:")




