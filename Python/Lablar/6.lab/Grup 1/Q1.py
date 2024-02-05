def euclidean(a, b):
    if a % b == 0:
        return b
    else:
        return euclidean(b, a % b)

try:
    sayi1 = int(input("Birinci sayıyı girin: "))
    sayi2 = int(input("İkinci sayıyı girin: "))
    if sayi2 == 0:
        print("Bir sayı sıfıra bölünemez.")
    else:
        print("En Büyük Ortak Bölen (EBOB):", euclidean(sayi1, sayi2))
except ValueError:
    print("Geçersiz giriş. Lütfen bir tamsayı girin.")
except Exception as e:
    print("Bir hata oluştu:", str(e))
