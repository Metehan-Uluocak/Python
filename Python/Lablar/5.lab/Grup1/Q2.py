def decimal_to_binary(decimal):
    if decimal < 0:
        return "Negatif sayılar için binary dönüşüm desteklenmez."
    elif decimal == 0:
        return "0"
    else:
        binary = ""
        while decimal > 0:
            remainder = decimal % 2
            binary = str(remainder) + binary
            decimal = decimal // 2
        return binary

try:
    
    sayi = int(input("Bir tamsayi girin: "))

    
    binary_sonuc = decimal_to_binary(sayi)
    print("Binary dönüşüm:", binary_sonuc)
except ValueError:
    print("Geçersiz giriş. Lütfen bir tamsayi girin.")
