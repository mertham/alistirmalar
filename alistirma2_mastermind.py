import random
sayi = random.randint(10,98)
while True : 
    if sayi % 11 == 0 :
        continue
    tahmin = input("2 basamaklı rakamları farklı bir sayi tahmin ediniz: ")
    if int(tahmin) % 11 == 0 or len(tahmin) != 2 :
        print("kurallara uyunuz")
        continue
    tahmin = int(tahmin)
    dogru_yer_sayaci = 0
    yanlis_yer_sayaci = 0
    a = sayi // 10
    b = sayi % 10 
    c = tahmin // 10
    d = tahmin & 10
    if a == c or b == d :
        dogru_yer_sayaci += 1
        print("doğru sayacı : ",dogru_yer_sayaci)
    if a != c and b !=d :
        yanlis_yer_sayaci += -1
        print("yanlış sayacı",yanlis_yer_sayaci)
    if a == c and b == d:
        print("dogru tahmin ettiniz. Programdan çıkılıyor..")
        break
