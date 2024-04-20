import random
from print_hangman import print_hangman

word_dictionary = ["queer", "music","python", "cat", "basketball", "football", "radio", "pizza", "sushi", "anime", "car", "capibara", "cherry"]
random_word_generator = random.choice(word_dictionary)

def print_word(guessedl):
    counter = 0
    rightl = 0
    for char in random_word_generator:
        if(char in guessedl):
            print(random_word_generator[counter], end=" ")
            rightl += 1
        else:
            print(" ", end=" ")
        counter += 1
    return rightl   
    

def print_lines():
    print("\n")
    for char in random_word_generator:
        print("\u203E", end=" ")


def gameplay():
    word_len = len(random_word_generator)
    guess_wrong = 0
    guess_index = 0   
    guess_letters = []
    all_letters = []
    guess_right = 0
    for x in random_word_generator:
        print("_", end=" ")
    while(guess_wrong != 6 and guess_right != word_len):
        print("\n\nLetters guessed so far: ")
        for letter in guess_letters:
            print(letter, end=" ")
        guessed = input("\n\nWrite your letter: ")
        while not guessed.isalpha():
            print("Error: You can only type letters. Try again!")
            guessed = input("\nWrite your letter: ")
        while guessed in all_letters:
            print("Error: You already tried that letter. Try again!")
            guessed = input("\nWrite your letter: ")
        all_letters.append(guessed)
        if(random_word_generator[guess_index] == guessed):
            print_hangman(guess_wrong)
            guess_index += 1
            guess_letters.append(guessed)
            guess_right = print_word(guess_letters)
            print_lines()
        else:
            guess_wrong += 1
            guess_letters.append(guessed)
            print_hangman(guess_wrong)
            guess_right = print_word(guess_letters)
            print_lines()
    if (guess_right == word_len):
        print("\nCongratulations, you won :)\n")
        beginning()
    else:
        print("\nSorry, you lost :(\n")
        beginning()


def beginning():
    option = input("Type in one of the above [New Game, Instructions, Exit]: ")
    commands = ["New Game", "Instructions", "Exit"]
    while(1):
        if (option == commands[0]):
            print("\n")
            gameplay()
        elif (option == commands[1]):
            print("\nThe game is pretty simple.\nYou have 6 chances to guess what word/letter is hidden under the lines.\nIf you manage to guess all of them right, you win.\nIf you guess wrong, the man will slowly die.\n")
            beginning()
        elif (option == commands[2]):
            a = input("Are you sure, that you want to Exit? (Yes/No): ")
            if (a == "Yes"):
                exit(0)
            elif(a == "No"):
                beginning()
        else:
            print("Error: Wrong command. Try again!")
            beginning()
            
print("Hello, and welcome to HangMan!")
print("------------------------------")
beginning()