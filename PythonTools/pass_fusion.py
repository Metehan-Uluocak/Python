import random
import argparse


def user_input():
    parser = argparse.ArgumentParser(description="Generate a wordlist.")
    parser.add_argument("-f", "--filename", dest="filename", help="Specify the filename")
    parser.add_argument("-w", "--wordcount", dest="wordcount", type=int,  help="Specify the number of words")
    args = parser.parse_args()

    print(r"""
 ____               _____          _             
|  _ \ __ _ ___ ___|  ___|   _ ___(_) ___  _ __  
| |_) / _` / __/ __| |_ | | | / __| |/ _ \| '_ \ 
|  __/ (_| \__ \__ \  _|| |_| \__ \ | (_) | | | |
|_|   \__,_|___/___/_|   \__,_|___/_|\___/|_| |_|
                                                 
Example Usage: python pass_fusion.py -f [wordlist.txt] -w [word count]
    """)

    print("Please enter the following information. Leave blank if you don't want to provide.")

    name = input("Name: ")
    surname = input("Surname: ")
    birth = input("Birth: ")
    pet = input("Pet: ")

    additional_info = input("Would you like to provide additional information? (yes/no): ")
    if additional_info.lower() == 'yes':
        print("Enter additional words one by one. Enter '-1' to finish.")
        word_list = [name, surname, birth, pet]
        while True:
            useful_info = input("Add a word: ")
            if useful_info == "-1":
                break
            elif useful_info == "":
                print("Please input one word at a time.")
            else:
                word_list.append(useful_info)
    else:
        word_list = [name, surname, birth, pet]

    if not args.filename:
        args.filename = input("Enter the filename: ")

    if not args.wordcount:
        args.wordcount = int(input("Enter the word count: "))

    if not args.filename:
        args.filename = "wordlist.txt"
    if not args.wordcount:
        args.wordcount = 100

    word_generator(word_list, args.filename, args.wordcount)

def word_generator(word_list, file_name, word_count):
    with open(file_name, "w") as file:
        generated_words = set()  
        priv_char = ["!","@","&","'","#","+","$","*","-","/"]
        for _ in range(word_count):
            word1 = random.choice(word_list)
            word2 = random.choice(word_list)
            
            new_word = word1 + word2 

            if random.choice([True, False]):
                new_word = str(random.randint(0, 9)) + new_word
            else:
                new_word += str(random.randint(0, 9))
            if random.choice([True, False]):
                if random.choice([True, False]):
                    new_word = str(random.choice(priv_char)) + new_word
                else:
                    if random.choice([True, False]):
                        index = random.randint(0, len(new_word))
                        new_word = new_word[:index] + random.choice(priv_char) + new_word[index:]
            if random.choice([True, False]):
                if random.choice([True, False]):
                    new_word = new_word[::-1]
            if random.choice([True, False]):
                if random.choice([True, False]):
                    new_word = new_word.lower()
                else:
                    new_word = new_word.upper()
            if new_word not in generated_words:
                file.write(new_word + "\n")
                generated_words.add(new_word)

if __name__ == "__main__":
    user_input()
