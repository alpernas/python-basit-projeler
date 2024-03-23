# toplama
"""
def toplama(*args):
    top=0
    for i in args:
        top+=i
    return top
print("toplamları:",toplama(1,4,6,2))

# faktöriyel hesapla
def faktöriyel(x):
    fakt=1
    for i in range(2,x+1):
        fakt*=i
    return fakt
print("faktöriyel:",faktöriyel(4))

#liste elemanlarını toplama
def toplama(list):
    return sum(list)
list1=[1,4,63,75,5,34]
print("toplam:",toplama(list1))

# asal sayı bulma
def asal_bul(x):
    if x==1:
        return False
    else:
        for i in range(2,x):
            if x%i==0:
                return False
        return True
while True:

     y=input("sayı gir:")
     if y=='q':
         break
     else:
         if asal_bul(int(y)):
             print(y,"sayısı asaldır")
         else:print(y,"sayısı asal degildir")

#fibonacci serisi
def fibonacci(x):
    f0=1
    f1=1
    print(f0,f1,)
    for i in range(2,x+1):
        fn=f0+f1
        print(fn)
        f0=f1
        f1=fn
print(fibonacci(4))

def büyük_bul(*args):
    return max(args)
print("enbüyük sayı:",büyük_bul(2,4,74,34))

# tam bölünüp bölünmedigini konntrol eden metod

def tam_böl(x,y):
    if x%y==0:
        return True
    else:
        return False

print(tam_böl(4,1))

#kelime sayısı bulma
def str_(cümle):
    kelimeler=cümle.split()
    return len(kelimeler)
print(str_("alper nas kayseri"))

def palindrom(x):
    if x==x[::-1]:
        return True
    else: False
print(palindrom(121))
"""