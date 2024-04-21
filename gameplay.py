import random
from print_hangman import print_hangman
from config import *
from utils import *

def gameplay(random_word_generator):
    word_len = len(random_word_generator)
    guess_wrong = 0
    guess_index = 0   
    guess_letters = []
    all_letters = []
    guess_right = 0
    for x in random_word_generator:
        print("_", end=" ")
    while(guess_wrong != 6 and guess_right != word_len):
        print(colors.CYAN + "\n\nLetters guessed so far: " + colors.RESET)
        for letter in guess_letters:
            print(letter, end=" ")
        guessed = input(colors.CYAN + "\n\nWrite your letter: " + colors.RESET)
        while not guessed.isalpha() and not guessed[:0]:
            print(colors.RED + "Error: You can only type letters. Try again!" + colors.RESET)
            guessed = input(colors.CYAN + "\nWrite your letter: " + colors.RESET)
        while guessed in all_letters:
            print(colors.RED + "\nError: You have already typed that letter. Try again!" + colors.RESET)
            guessed = input(colors.CYAN + "\nWrite your letter: " + colors.RESET + colors.RESET)
        all_letters.append(guessed)
        if(random_word_generator[guess_index] == guessed):
            print_hangman(guess_wrong)
            guess_index += 1
            guess_letters.append(guessed)
            guess_right = print_word(guess_letters, random_word_generator)
            print_lines(random_word_generator)
        else:
            guess_wrong += 1
            guess_letters.append(guessed)
            print_hangman(guess_wrong)
            guess_right = print_word(guess_letters, random_word_generator)
            print_lines(random_word_generator)
    if (guess_right == word_len):
        print(colors.YELLOW + "\nCongratulations, you won :)\n" + colors.RESET)
        beginning()
    else:
        print(colors.YELLOW + "\nSorry, you lost :(\n" + colors.RESET)
        print("The hidden word was: " + colors.YELLOW + random_word_generator + colors.RESET)
        beginning()


def beginning():
    option = input("Type in one of the above [start, instructions, exit]: ")
    commands = ["start", "instructions", "exit"]
    while(1):
        if (option == commands[0]):
            print("\n")
            random_word_generator = category()
            gameplay(random_word_generator)
        elif (option == commands[1]):
            print("\nThe game is pretty simple.\nYou have " + colors.YELLOW + "6 chances to guess " + colors.RESET + "what word/letter is hidden under the lines.\nIf you manage to guess all of them " + colors.YELLOW + "right, you win" + colors.RESET + ".\nIf you guess " + colors.YELLOW + "wrong, you lose," + colors.RESET + " and the man slowly starts to die.\n")
            beginning()
        elif (option == commands[2]):
            a = input(colors.YELLOW + "Are you sure, that you want to Exit? (Yes/No): " + colors.RESET)
            if (a == "Yes"):
                exit(0)
            elif(a == "No"):
                beginning()
        else:
            print(colors.RED + "Error: Wrong command. Try again!" + colors.RESET)
            beginning()