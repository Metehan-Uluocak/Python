import ast

def sum_of_even_and_odd(lst):
    odd, even = 0, 0
    for i in lst:
        if i % 2:
            odd += i
        else:
            even += i
    return [even, odd]

try:
    line = input("Bir liste girin (örneğin, [1, 2, 3]): ")
    lst = ast.literal_eval(line)
    
    if isinstance(lst, list):
        print("Çift ve Tek Sayıların Toplamı:", sum_of_even_and_odd(lst))
    else:
        print("Geçersiz giriş. Lütfen bir liste girin.")
except Exception as e:
    print("Bir hata oluştu:", str(e))
