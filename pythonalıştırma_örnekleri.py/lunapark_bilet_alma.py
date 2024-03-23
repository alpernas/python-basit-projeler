boy=int(input("boyunuzu giriniz:"))
bilet=None
if boy>120:
    yaş=int(input("yaşınzı giriniz:"))
    if yaş<12:
        bilet=15
        print("bilet fiyatınız:{}".format(bilet))
    elif yaş>=12 or yaş<=18:
        bilet=25
        print("bilet fiyatınız:{}".format(bilet))
    else:
        bilet=35
        print("bilet fiyatınız:{}".format(bilet))

else: print("boyunuz kıssa hızlı trene binemessiniz.")


