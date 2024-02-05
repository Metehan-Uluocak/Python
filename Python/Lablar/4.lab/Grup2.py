import math


m2_fiyatlari = {
    34: 5000,
    23: 4500,
    35: 4000,
    33: 3500,
    55: 3000
}


sehirKodu = int(input("Sehir Kodu: "))
evinMetreKaresi = int(input("Evin Metre Karesi: "))
pesinat = int(input("Pesinat: "))
yillikFaiz = float(input("Yillik Faiz: "))
taksitSayisi = int(input("Taksit Sayisi: "))
yazdirmakIstenenTaksitSayisi = int(input("Yazdirmak Istenen Taksit Sayisi: "))


evinMetreKareFiyati = m2_fiyatlari.get(sehirKodu, 0)


evinFiyati = evinMetreKaresi * evinMetreKareFiyati


aylikFaiz = yillikFaiz / (12 * 100)


aylikTaksitMiktari = (evinFiyati - pesinat) * aylikFaiz * pow(1 + aylikFaiz, taksitSayisi) / (pow(1 + aylikFaiz, taksitSayisi) - 1)

kontrol = 1
print("Aylik Taksit Miktari: {:.2f}".format(aylikTaksitMiktari))


while kontrol <= yazdirmakIstenenTaksitSayisi:
    kalanBorc = evinFiyati - pesinat
    odenecekFaizMiktari = kalanBorc * aylikFaiz
    odenecekAnaparaMiktari = aylikTaksitMiktari - odenecekFaizMiktari

    print("Kalan Borc: {:.2f}".format(kalanBorc))
    print("Odenecek Faiz Miktari: {:.2f}".format(odenecekFaizMiktari))
    print("Odenecek Anapara Miktari: {:.2f}".format(odenecekAnaparaMiktari))

   
    kalanBorc -= aylikTaksitMiktari

    kontrol += 1
