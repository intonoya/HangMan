import random
from print_hangman import print_hangman
from config import *


def category():
    a = input("Choose one of the categories [sport, animals, music, random, hardcore]: ")
    if (a == "sport"):
        random_word_generator = random.choice(word_sport)
    elif (a == "animals"):
        random_word_generator = random.choice(word_animals)
    elif (a == "music"):
        random_word_generator = random.choice(word_music)
    elif (a == "random"):
        random_word_generator = random.choice(word_random)
    elif (a == "hardcore"):
        random_word_generator = random.choice(word_hard)
    else:
        print(colors.RED + "Error: You can only choose from one of the above. Try again!" + colord.RESET)
        category()
    return (random_word_generator)


def print_word(guessedl, random_word_generator):
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
    

def print_lines(random_word_generator):
    print("\n")
    for char in random_word_generator:
        print("\u203E", end=" ")
        
