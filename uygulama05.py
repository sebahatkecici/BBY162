import random

renkler = random.choice(['mavi', 'mor', 'sarı', 'beyaz', 'kahverengi', 'lacivert', 'siyah', 'kırmızı', 'turuncu','gri'])
kelimeler = []
can = 6
boşluklar = '_'

boşluksayısı = list(boşluklar * len(renkler))

dongu = 1

while dongu:
    print(' '.join(boşluksayısı), end='\n\n')

    seçilenharf= input('Harf Giriniz').lower()

    try:
        int(seçilenharf)
        print('Lütfen bir harf giriniz.\n')
    except:
        if len(seçilenharf) > 1:
            print('HARF giriniz!\n')
        else:
            if seçilenharf in kelimeler:
                print('Bu harfi zaten girdiniz.\n')
            else:
                doğru = None
                for i in range(len(renkler)):
                    if seçilenharf == renkler[i]:
                        doğru = True

                        boşluksayısı[i] = seçilenharf

                        kelimeler.append(seçilenharf)

                        if boşluklar not in boşluksayısı:
                            print(' '.join(boşluksayısı))
                            print('\nTebrikler oyunu kazandınız')

                            dongu = 0

                else:

                    if doğru != True:
                        can -= 1

                        print('Yanlış harf. Kalan hakkınız: {}\n'.format(can))

                kelimeler.append(seçilenharf)

                if can == 0:
                    print(' Oyunu Kaybettiniz. Seçilen kelime "{}" idi.\n'.format(renkler))

                    break