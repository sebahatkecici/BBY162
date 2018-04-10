import random

secilenKelime = random.choice(["pembe", "mor", "kırmızı", "mavi", "turuncu", "beyaz", "lacivert", "sarı", "yeşil", "gri"])
hakSayısı = 3
cizgi = "_"
panoKelime =[]
print("Adam Asmaca oyununa Hoşgeldiniz..\n")

for kelime in secilenKelime:

    panoKelime.append(cizgi)

print(panoKelime)

while hakSayısı > 0:

    i = 0

    girilenHarf = input("\nBir harf giriniz: ").lower()

    if girilenHarf in secilenKelime:
        for kontrol in secilenKelime:
            if secilenKelime[i] == girilenHarf:
                panoKelime[i] = girilenHarf
            i += 1

        print("")
        print(panoKelime)
        print('Doğru harf girdiniz.')

    else:
        hakSayısı -= 1
        print("")
        print(panoKelime)
        print("Yanlış harf girdiniz.")
        print("\nKalan hak sayısı="+str(hakSayısı))

    if hakSayısı == 0:
        print('oyunu kaybettiniz.Doğru cevap"{}" idi.\n'.format(secilenKelime))
        break

    if cizgi not in panoKelime:
        print("\nTebrikler! Kelimeyi buldunuz Oyunu Kazandınız!")
        break


