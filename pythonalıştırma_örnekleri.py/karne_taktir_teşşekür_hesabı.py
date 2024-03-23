sınav1=int(input("1. sınavı giriniz:"))
sınav2=int(input("2. sınavı giriniz:"))
ort=(sınav1+sınav2)/2
if ort>=85:
    print("tebrikler taktir aldınız ort:{}".format(ort))
elif ort>=70 and ort<85:
    print("tebrikler teşekkür aldınız ort:{}".format(ort))
else:
    print("malesef belge alamıyorsunuz ort:{}".format(ort))