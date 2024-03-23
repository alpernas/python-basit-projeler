while True:
     top=0
     sayı=int(input("sayı giriniz:"))

     for i in str(sayı):
         top=int(i)**len(str(sayı))
     if sayı!=top:
            print(f"{sayı} sayısı armgstrong sayı degildir")
     else:
            print(f"{sayı} armstrong sayı girdiniz")
            break