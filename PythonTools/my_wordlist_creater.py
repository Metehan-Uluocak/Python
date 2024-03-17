import random
import argparse

def user_input():
    parser = argparse.ArgumentParser(description="Generate a wordlist.")
    parser.add_argument("-f", "--filename", dest="filename", help="Specify the filename")
    parser.add_argument("-w", "--wordcount", dest="wordcount", type=int, help="Specify the number of words")
    args = parser.parse_args()

    name = input("Name: ")
    surname = input("Surname: ")
    birth = input("Birth: ")
    pet = input("Pet: ")

    word_list = [name, surname, birth, pet]

    useful_info = None
    while useful_info != "-1":
        useful_info = input("Add some words you think are useful (One by one). Enter -1 to exit: ")
        if useful_info == "-1":
            break
        elif useful_info == "":
            print("Please input one word at a time. Try again.")
        else:
            word_list.append(useful_info)

    if not args.filename:
        file_name = input("Enter the filename: ")
    else:
        file_name = args.filename

    if not args.wordcount:
        word_count = int(input("Enter the word count: "))
    else:
        word_count = args.wordcount

    word_generator(word_list, file_name, word_count)

def word_generator(word_list, file_name, word_count):
    with open(file_name, "w") as file:
        generated_words = set()  
        for _ in range(word_count) :
            word1 = random.choice(word_list)
            word2 = random.choice(word_list)
            
            new_word = word1 + word2 

            # Randomly choose whether to add numbers to the beginning or end
            if random.choice([True, False]):
                new_word = str(random.randint(0, 9)) + new_word
            else:
                new_word += str(random.randint(0, 9))
                
            if new_word not in generated_words:
                file.write(new_word + "\n")
                generated_words.add(new_word)

if __name__ == "__main__":
    user_input()
