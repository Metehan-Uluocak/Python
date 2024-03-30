import random
import argparse


def user_input():
    parser = argparse.ArgumentParser(description="Generate a wordlist.")
    parser.add_argument("-f", "--filename", dest="filename", help="Specify the filename")
    parser.add_argument("-w", "--wordcount", dest="wordcount", type=int, help="Specify the number of words")
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

    word_list = []
    if name:
        word_list.append(name)
    if surname:
        word_list.append(surname)
    if birth:
        word_list.append(birth)
    if pet:
        word_list.append(pet)

    additional_info = input("Would you like to provide additional information? (yes/no): ")
    if additional_info.lower() == 'yes':
        print("Enter additional words one by one. Enter '-1' to finish.")
        while True:
            useful_info = input("Add a word: ")
            if useful_info == "-1":
                break
            elif useful_info == "":
                print("Please input one word at a time.")
            else:
                word_list.append(useful_info)

    if not args.filename:
        args.filename = input("Enter the filename: ")

    if not args.wordcount:
        args.wordcount = int(input("Enter the word count: "))

    if not args.filename:
        args.filename = "wordlist.txt"
    if not args.wordcount:
        args.wordcount = 100

    word_generator(word_list, args.wordcount, args.filename)


def word_generator(word_list, word_count, filename):
    priv_char = ["!", "@", "&", "'", "#", "+", "$", "*", "-", "/"]
    generated_words = set()  
    loop_count = word_count
    with open(filename, "a", encoding="utf-8") as file:
        while loop_count > 0:
            word1 = random.choice(word_list)
            word2 = random.choice(word_list)
            compound_word = word1 + word2
            
            passlist = [word1, word2, compound_word]
            testword = random.choice(passlist)

            if random.choice([True, False]):
                new_word = str(random.randint(0, 9)) + testword
            else:
                testword += str(random.randint(0, 9))
            if random.choice([True, False]):
                if random.choice([True, False]):
                    index = random.randint(0, len(testword))
                    new_word = testword[:index] + random.choice(priv_char) + testword[index:]
                else:
                    new_word = str(random.choice(priv_char)) + testword
            if random.choice([True, False]):
                if random.choice([True, False]):
                    new_word = testword[::-1]
            if random.choice([True, False]):
                if random.choice([True, False]):
                    new_word = testword.lower()
                else:
                    new_word = testword.upper()
                    
            if new_word not in generated_words:
                generated_words.add(new_word)
                file.write(new_word + "\n")
                loop_count -= 1

if __name__ == "__main__":
    user_input()
