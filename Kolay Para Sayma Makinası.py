print("""Kolay Para Sayma Makinası, version 1.0 -release (x86_x64)
Licence GPLv3+ : GNU GPL version 3 <https://www.gnu.org/licenses/gpl-3.0.html>
copyright (C) 2022 BatuHanHub Software 

This is free software; you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.""")

print("Kolay Para Sayma Programına Hoşgeldiniz!\n")

while True:

    ikiYuz=int(input("kaç tane 200tl niz var:"))
    
    if ikiYuz > 0:
        pass
    elif ikiYuz < 0:
        print("\nhata:lütfen sayı giriniz\n")
        continue
    
    yuz=int(input("kaç tane 100tl niz var:"))
    
    if yuz > 0:
        pass
    elif yuz < 0:
        print("\nhata:lütfen sayı giriniz\n")
        continue
    
    elli=int(input("kaç tane 50tl niz var:"))
    
    if elli > 0:
        pass
    elif elli < 0:
        print("\nhata:lütfen sayı giriniz\n")
        continue
    
    yirmi=int(input("kaç tane 20tl niz var:"))
    
    if yirmi > 0:
        pass
    elif yirmi < 0:
        print("\nhata:lütfen sayı giriniz\n")
        continue
    
    on=int(input("kaç tane 10tl niz var:"))
    
    if on > 0:
        pass
    elif on < 0:
        print("\nhata:lütfen sayı giriniz\n")
        continue
    
    bes=int(input("kaç tane 5tl niz var:"))
    
    if bes > 0:
        pass
    elif bes < 0:
        print("\nhata:lütfen sayı giriniz\n")
        continue
    
    bir=int(input("kaç tane 1tl niz var:"))
    
    if bir > 0:
        pass
    elif bir < 0:
        print("\nhata:lütfen sayı giriniz\n")
        continue

    islem1= ikiYuz * 200
    islem2= yuz * 100
    islem3= elli * 50
    islem4= yirmi * 20
    islem5= on * 10
    islem6= bes * 5
    islem7= bir * 1

    sonuc1= islem1 + islem2 + islem3 + islem4 + islem5 + islem6 + islem7

    print("toplam paranız:", sonuc1)

    print("\ndiğer projelerim için: <https://github.com/BatuHanHub>")

    input("Cıkmak icin bir tusa basınız...")
