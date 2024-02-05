import ast

def sum_fractions(lst):
    total_sum = 0
    for fraction in lst:
        numerator, denominator = fraction
        total_sum += numerator / denominator
    return int(total_sum)


input_line = input("İlk kesiri girin (örneğin, [18, 13]): ")
fraction1 = ast.literal_eval(input_line)


input_line = input("İkinci kesiri girin (örneğin, [4, 5]): ")
fraction2 = ast.literal_eval(input_line)

fractions = [fraction1, fraction2]

result = sum_fractions(fractions)
print("Kesirlerin Toplamı (Tam Sayı):", result)
