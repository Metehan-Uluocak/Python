def binary_to_decimal(binary):
    decimal = 0
    binary = binary[::-1]  
    
    for i in range(len(binary)):
        if binary[i] == '1':
            decimal += 2**i
    
    return decimal

try:
    
    binary_sayi = input("Bir binary sayı girin: ")


    decimal_sonuc = binary_to_decimal(binary_sayi)
    print("Ondalık dönüşüm:", decimal_sonuc)
except ValueError:
    print("Geçersiz giriş. Lütfen bir binary sayı girin.")
except Exception as e:
    print("Bir hata oluştu:", str(e))
