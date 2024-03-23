import time
from datetime import  date
top=0
while True:

    sayı=input("sayı:")
    if sayı=="q":
        print("çıkış yapıyorsunuz..")
        time.sleep(2)
        print("çıkış yaptınız.")
        break
    else:
        top+=int(sayı)
print("toplamları:",top)