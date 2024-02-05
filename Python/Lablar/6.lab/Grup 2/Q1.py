def sum_digits(n):
    if n < 10:
        return n
    else:
        return sum_digits(sum(int(digit) for digit in str(n)))

try:
    sayi = int(input("Bir sayı girin: "))
    print("Rakamların Toplamı:", sum_digits(sayi))
except ValueError:
    print("Geçersiz giriş. Lütfen bir sayı girin.")
