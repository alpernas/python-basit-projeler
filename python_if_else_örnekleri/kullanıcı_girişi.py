import time
from datetime import date
print("""
**********
Kullanıcı Girişi
**************
""")
System_kullanıcı_adı="33316567622"
system_parola="Alper2961"
kullanıcı=input("kullanıcı adı:")
parola=input("parola:")
if System_kullanıcı_adı==kullanıcı and system_parola!=parola:
    print("parolayı kontrol ediniz")
elif System_kullanıcı_adı!=kullanıcı and system_parola==parola:
    print("kullanıcı adı kontrol ediniz")
elif System_kullanıcı_adı!=kullanıcı and system_parola!=parola:
    print("kullanıcı adı ve parolayı kontrol ediniz")
else:
    print("sisteme giriş yapılıyor...")
    time.sleep(2)
    print("tebrikler sisteme girişyaptınız")

