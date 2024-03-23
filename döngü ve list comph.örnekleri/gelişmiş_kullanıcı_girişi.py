print("""
***************
kullanıcı girişi programı
*************
""")
sys_kullanıcı_adı="33316567622"
sys_parola="alper2961"
giriş_hakkı = 3

while True:
    kullanıcı=(input("kullanıcı adı:"))
    parola=(input("parola:"))
    if sys_kullanıcı_adı==kullanıcı and sys_parola!=parola:
        print("parolanızı kontrol ediniz")
        giriş_hakkı-=1

        tuş=input("parolayı unuttuysanız 1 tuşuna basınız yoksa devam etmek için 0 a basınız")
        if tuş=="1":
            tel=input("lütfen geçerli telefon giriniz:")
            if tel=="05376922902":
                sys_kullanıcı_adı=input("yeni kullanıcı adınızı giriniz:")
                sys_parola=input("yeni parola giriniz:")
            else:print("hatalı telefon numarası girdiniz:")

    elif sys_kullanıcı_adı!=kullanıcı and sys_parola==parola:
        print("kullanıcı adınızı kontrol ediniz")
        giriş_hakkı-=1
        tuş=input("parolayı unuttuysanız 1 tuşuna basınız yoksa devam etmek için 0 a basınız")
        if tuş=="1":
            tel=input("lütfen geçerli telefon giriniz:")
            if tel=="05376922902":
                sys_kullanıcı_adı = input("yeni kullanıcı adınızı giriniz:")
                sys_parola = input("yeni parola giriniz:")
            else:print("hatalı telefon numarası girdiniz:")
    elif sys_kullanıcı_adı != kullanıcı and sys_parola != parola:
        print("kullanıcı adınızı ve parolayı kontrol ediniz")
        giriş_hakkı -= 1
        tuş = input("parolayı unuttuysanız 1 tuşuna basınız yoksa devam etmek için 0 a basınız")
        if tuş == "1":
            tel = input("lütfen geçerli telefon giriniz:")
            if tel == "05376922902":
                sys_kullanıcı_adı = input("yeni kullanıcı adınızı giriniz:")
                sys_parola = input("yeni parola giriniz:")
            else:
                print("hatalı telefon numarası girdiniz:")
    else:
        print("tebrikler dogru giriş yaptınız")
        break
    if giriş_hakkı==0:
        print("giriş hakınız bitti")
        break
