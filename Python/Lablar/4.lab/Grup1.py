import math

while True:
    
    evinM2Fiyati = int(input("Evin Metre Kare Fiyati: "))
   

    if evinM2Fiyati == -1:
        break
    
    evinM2Alani = int(input("Evin Metre Karesi: "))
    evinVergiOrani = int(input("Evin Vergi Orani: "))
    aylikTaksitLimiti = int(input("Aylik Odenebilecek Taksit: "))
    peşinatMiktari = int(input("Peşinat: "))
    yillikFaizOrani = int(input("Yillik Faiz: "))
    taksitSayisi = int(input("Taksit Sayisi: "))
    
    
    evinFiyati = (evinM2Alani * evinM2Fiyati) + (evinM2Alani * evinM2Fiyati) * evinVergiOrani / 100
    print("Evin Fiyati: ", int(evinFiyati))

    aylikFaizOrani = yillikFaizOrani / (12 * 100)
    print("Aylik Faiz: {:.4f}".format(aylikFaizOrani))

    aylikTaksitMiktari = (evinFiyati - peşinatMiktari) * (aylikFaizOrani * math.pow(1 + aylikFaizOrani, taksitSayisi) / ((math.pow(1 + aylikFaizOrani, taksitSayisi) - 1)))
    print("Aylik Taksit Miktari: {:.2f}".format(aylikTaksitMiktari))

    print("true" if aylikTaksitMiktari <= aylikTaksitLimiti else "false")
