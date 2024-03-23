def polindrom(n):
    if n==n[::-1]:
        return True
    else: return False

sayı=(input("sayı giriniz:"))
if polindrom(sayı):
    print("sayınız polindromdur")
else: print("sayınız polindrom degildir")
