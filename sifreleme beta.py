#sifreleme programı beta
#29 adet random sayı içeren liste oluşturuyorum
import random
kod_sayilar = random.sample(range(0,29),29)
#bu listeye alfabenin harflerini atıyorum
kodharfsayi={}
for i,j in zip(range(0,29),"abcçdefgğhıijklmnoöprsştuüvyz") :
    kodharfsayi[kod_sayilar[i]] = j
#metni sayısal olarak görebilmek için sözlük oluşturuyorum
sözlük = {}
for i,j in zip("abcçdefgğhıijklmnoöprsştuüvyz",range(0,29)) :
    sözlük[i] = j
#metni input olarak alıyorum
text1 = input("şifrelemek istediğiniz metni giriniz: ")
#metindeki boşlukları kaldırıyorum
text1 = text1.replace(" ","")
#metnin elemanlarını listeye atıyorum
text = []
for i in text1:
    text.append(i)
#metni dönüştürüp yazdırıyorum
for i in range(0,len(text)):
    text[i]=kodharfsayi[sözlük[text[i]]]
print("".join(text))

def koduyazdır():
    alfabeliste = []
    for i in "abcçdefgğhıijklmnoöprsştuüvyz":
        alfabeliste.append(i)
    
    print("kodu oluşturmak için")

    for x in range(0,29):
        print(""" {} : {} """.format(alfabeliste[x],kodharfsayi[sözlük[alfabeliste[x]]]))
