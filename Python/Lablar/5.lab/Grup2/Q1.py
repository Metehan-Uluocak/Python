def my_cipher_reverse(txt):
    result, previous = '', 0
    for i in txt:
        if i.isalpha() and not previous:
            result += i
            previous = ord(i) - 64
        elif i.isalpha() and previous:
            current = ord(i) - 64
            current = (current - previous) % 26
            result += chr(current + 64)
            previous = current
        else:
            result += i

    return result.lower()

try:
    text = input("Bir metin girin: ")

    
    reversed_text = my_cipher_reverse(text)
    
  
    print("Çözülen Metin:", reversed_text)
except Exception as e:
    print("Bir hata oluştu:", str(e))

