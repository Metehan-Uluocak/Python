def my_cipher(txt):
    result, previous = '', 0
    for i in txt.upper():
        if i.isalpha() and not previous:
            result += i
            previous = ord(i) - 64
        elif i.isalpha() and previous:
            current = ord(i) - 64
            result += chr(((previous + current) % 26) + 64)
            previous = current
        else:
            result += i
    return result


text = input("Metin girin: ")


ciphered_text = my_cipher(text)


print("Sifrelenmis Metin:", ciphered_text)
