#YAZAR: Batuhan Uysalar

#Hatalar
def hata1():
    print('HATA:Lütfen pozitif sayı yazınız. "1,2,3..."')

      
print ( """
   _____ _____  _        ____         ___  
  / ____|  __ \| |      |___ \       / _ \ 
 | |  __| |__) | |        __) |     | | | |
 | | |_ |  ___/| |       |__ <      | | | |
 | |__| | |    | |____   ___) |  _  | |_| |
  \_____|_|    |______| |____/  (_)  \___/ 
                                        
Kolay Para Sayma Programı, sürüm 3.0 -sürüm (x86_x64)
Lisans GPLv3+ : GNU GPL sürüm 3 <https://www.gnu.org/licenses/gpl-3.0.html>
telif hakkı (C) 2022 BatuHanHub 

Bu ücretsiz bir yazılımdır; değiştirmekte ve yeniden dağıtmakta özgürsünüz.
Yasaların izin verdiği ölçüde HİÇBİR GARANTİ YOKTUR.\n""" )

print("Kolay Para Sayma Programına Hoşgeldiniz!\n")

while True:

    # Türk Liraları

    # 200 TL
    TL200 = int(input("kaç tane 200 TL niz var:"))

    if TL200 < 0:
        hata1()
        continue

    else:
        tpl200TL = 200 * TL200
        pass


    #100 TL
    TL100 = int(input("kaç tane 100 TL niz var:"))

    if TL100 < 0:
        hata1()
        continue

    else:
        tpl100TL = 100 * TL100
        pass


    #50 TL
    TL50  = int(input("kaç tane 50 TL niz var:"))

    if TL50 < 0:
        print("HATA:Lütfen pozitif sayı yazınız '1,2,3 gibi'")
        continue

    else:
        tpl50TL = 50 * TL50
        pass


    #20 TL
    TL20 = int(input("kaç tane 20 TL niz var:"))

    if TL20 < 0:
        hata1()
        continue

    else:
        tpl20TL = 20 * TL20
        pass


    #10 TL
    TL10  = int(input("kaç tane 10 TL niz var:"))

    if TL10 < 0:
        hata1()
        continue

    else:
        tpl10TL = 10 * TL10
        pass


    #5 TL
    TL5   = int(input("kaç tane 5 TL niz var:"))

    if TL5 < 0:
        hata1()
        continue

    else:
        tpl5TL = 5 * TL5
        pass


    #1 TL
    TL1   = int(input("kaç tane 1 TL niz var:"))

    if TL1 < 0:
        hata1()
        continue

    else:
        tpl1TL = 1 * TL1
        pass


    print("\nHadi şimdi Kuruş hesaplayalım!\n")

    #50 krş
    KRS50 = int(input("kaç tane 50 Kuruşunuz var:"))

    if KRS50 < 0:
        hata1()
        continue

    else:
        tpl50KRS = 0.50 * KRS50

        if tpl50KRS >= 100:
            tpl50KRS / 100
            pass

        else:
            pass

    #25 krş

    KRS25 = int(input("kaç tane 25 Kuruşunuz var:"))

    if KRS25 < 0:
        hata1()
        continue

    else:
        tpl25KRS = 0.25 * KRS25

        if tpl25KRS >= 100:
            tpl25KRS / 100
            pass

        else:
            pass

    #10 krş

    KRS10 = int(input("kaç tane 10 Kuruşunuz var:"))

    if KRS10 < 0:
        hata1()
        continue

    else:
        tpl10KRS = 0.10 * KRS10

        if tpl10KRS >= 100:
            tpl10KRS / 100
            pass

        else:
            pass

    KRS5 = int(input("kaç tane 5 Kuruşunuz var:"))

    if KRS5 < 0:
        hata1()
        continue

    else:
        tpl5KRS = 0.5 * KRS5

        if tpl5KRS >= 100:
            tpl5KRS / 100
            pass

        else:
            pass

    KRS1 = int(input("kaç tane 1 Kuruşunuz var:"))

    if KRS1 < 0:
        hata1()
        continue

    else:
        tpl1KRS = 0.01 * KRS1

        if tpl1KRS >= 100:
            tpl1KRS / 100
            pass

        else:
            pass

    break

toplam1 = tpl200TL+tpl100TL+tpl50TL+tpl20TL+tpl10TL+tpl5TL+tpl1TL
toplam2 = tpl50KRS+tpl25KRS+tpl10KRS+tpl5KRS+tpl1KRS
toplam3 = toplam1 + toplam2

print(f"toplam paranız '{toplam3}'dır.".format(toplam3))

input("diğer projelerim için 'https://github.com/BatuHanHub' çıkmak için bir tuşa basınız")
