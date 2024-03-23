v=50
t=0
while t<=9:
    if t<=4 and t>=0:
        x=v*t
        print(x)
    elif t>=4 and t<=9:
        x=5*t*t+90*t-80
        print(x)
    t+=1