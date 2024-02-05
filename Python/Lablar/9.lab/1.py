def is_inside(d, end, start):
    if start == end:
        return True
    for k, v in d.items():
        if start in v:
            return is_inside(d, end, k)
    else:
        return False


folder_system_example = {
    "A": ["B", "C", "D"],
    "B": ["E", "F"],
    "D": ["G", "H"],
    "G": ["I", "J"],
    "H": ["K"]
}

while True:
    user_input = input("İki klasörü virgülle ayırarak girin (örn. B,A) veya 'q' girerek çıkın: ").strip().split(",")

    if user_input[0].lower() == "q":
        break


    if len(user_input) != 2 or user_input[0] not in folder_system_example or user_input[1] not in folder_system_example:
        print("Geçersiz giriş! Lütfen doğru klasör isimleri girin.")
        continue

    result = is_inside(folder_system_example, user_input[1], user_input[0])
    print(result)
