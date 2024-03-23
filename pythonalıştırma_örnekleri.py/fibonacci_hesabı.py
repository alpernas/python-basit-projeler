sayı=int(input("sayı giriniz:"))
f1=1
f2=2
fn=None
print(f1," ",f2)
for i in range(2,sayı+1):
    fn=f1+f2
    print(" ",fn)
    f1=f2
    f2=fn

