def bubble_sort_step_by_step(arr):
    n = len(arr)
    
    print("Orijinal Liste:", arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                
                arr[j], arr[j+1] = arr[j+1], arr[j]

                
                print(f"Adım {i+1}.{j+1}:", arr)

def get_integer_list_from_input():
    while True:
        try:
            user_input = input("Liste elemanlarını boşluklu bir şekilde girin: ")
            integer_list = [int(x) for x in user_input.split()]
            return integer_list
        except ValueError:
            print("Hatalı giriş. Lütfen sayıları doğru bir şekilde girin.")

my_list = get_integer_list_from_input()


bubble_sort_step_by_step(my_list.copy())
