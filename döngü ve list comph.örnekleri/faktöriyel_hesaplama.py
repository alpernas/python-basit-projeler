print("""
*****************

Faktöriyel bulma programı

çıkmak için 'q' ya basınız.
******************
""")

while True:
    sayı=input("sayı:")
    if sayı=='q':
        print("program sonlandırılıyor..")
        break
    else:
        sayı=int(sayı)
        fakt=1
        for i in range(1,sayı+1):
            fakt*=i
        print("sonuç:",fakt)
