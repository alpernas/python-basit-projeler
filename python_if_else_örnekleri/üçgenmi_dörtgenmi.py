giriş=input("üçgen ise 1 dörtgen ise 2 ye basınız:")
if giriş=="2":
    print("dört kenarıda sırasıyla giriniz")
    kenar1=int(input())
    kenar2=int(input())
    kenar3=int(input())
    kenar4=int(input())
    if kenar1==kenar2 and kenar1==kenar3 and kenar1==kenar4:
        print("karedir")
    elif (kenar1 == kenar2 or kenar1==kenar3 or kenar1==kenar4) and (kenar2==kenar1 or
    kenar2==kenar3 or kenar2==kenar4) :
        print("dikdörtgendir")
    else:
        print("çeşit kenar dır")
elif giriş=="1":
    print("üç kenarıda sırasıyla giriniz:")
    kenar1=int(input())
    kenar2=int(input())
    kenar3=int(input())
    if abs(kenar1+kenar2)>kenar3 and abs(kenar1+kenar3)>kenar2 and abs(kenar2+kenar3)>kenar1:
        if kenar1==kenar2 and kenar1==kenar3:
            print("eş kenar üçgen")
        elif (kenar2==kenar3 and kenar2!=kenar1) or (kenar2==kenar1 and kenar2!=kenar3) or(kenar1==kenar2 and
        kenar1!=kenar3 ):
            print("ikiz kenar")
        else: print("çeşitkenar")
    else:
        print("üçgen belirtmiyor")
else: print("geçersiz işlem girdiniz:")


