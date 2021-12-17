import csv
import random

# Creates the unique User ID using the random module
user_id = str(random.randint(1000, 9999))

encryption_values = {'a': '1', 'b': '2', 'c': '3', 'd': '?', 'e': '?', 'f': '?',
                     'g': '?', 'h': '?', 'i': '?', 'j': '?', 'k': '?', 'l': '?',
                     'm': '?', 'n': '?', 'o': '?', 'p': '?', 'q': '?', 'r': '?',
                     's': '?', 't': '?', 'u': '?', 'v': '?', 'w': '?', 'x': '?',
                     'y': '?', 'z': '?', 'A': '?', 'B': '?', 'C': '?', 'D': '?',
                     'E': '?', 'F': '?', 'G': '?', 'H': '?', 'I': '?', 'J': '?',
                     'K': '?', 'L': '?', 'M': '?', 'N': '?', 'O': '?', 'P': '?',
                     'Q': '?', 'R': '?', 'S': '?', 'T': '?', 'U': '?', 'V': '?',
                     'W': '?', 'X': '?', 'Y': '?', 'Z': '?', '0': '?', '1': '?',
                     '2': '?', '3': '?', '4': '?', '5': '?', '6': '?', '7': '?',
                     '8': '?', '9': '?'}


def user_id_generator():
    print("Please generate your unique User ID# below")
    start_prompt = input("Enter 'Y' to generate unique User ID: ")

    if start_prompt == "Y" or start_prompt == "y":
        print(f"Your unique User ID is {user_id}")
    else:
        print("Please enter valid response!")
        user_id_generator()


# Encrypts the phrase entered by the user
def password_generator():
    user_phrase = input("Please enter phrase to be encrypted: ")
    phrase_split = list(user_phrase)

    for i in phrase_split:
        if i in encryption_values:
            print(encryption_values.values())


user_id_generator()
password_generator()
