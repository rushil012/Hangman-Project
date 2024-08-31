# assignment: programming assignment 1
# author: Rushil Nagpal
# date: 10th April, 2023
# file: hangman.py is a program that is a game where player has to guess the word correctly 
# by choosing his choice of size of the word and lives.
# input: taking word from file "dictionary.txt".
# output: making the player make some choices and guess the word.

from random import choice, random

dictionary_file = "dictionary.txt"

def import_dictionary(filename) :
    dictionary = {}
    max_size = 12
    try:
        with open(dictionary_file) as fh:
            z = fh.readlines()
            ll = []
            for k in z:
                l = k.strip()
                ll.append(l)
        
            for i in range(3,13):
                p = []
                for k in ll:
                    if len(k) == i:
                        p.append(k)
                dictionary[i] = p
    except KeyError:
        l = dictionary[12]
        for pll in ll:
            if len(pll) > 12:
                l.append(pll)
        dictionary[12] = l
    return dictionary

def get_game_options():
    size = int(input("Please choose a size of a word to be guessed [3 - 12, default any size]: \n"))
    try:
        if size in range(3,13):
            print(f'The word size is set to {size}.')
    except :
        print("A dictionary word of any size will be chosen.")
        size = choice(range(3,13))
    else:
        print("A dictionary word of any size will be chosen.")
        size = choice(range(3,13))

    lives = int(input("Please choose a number of lives [1 – 10, default 5]: \n"))
    if lives in range(1,11):
        print(f'You have {lives} lives.')
    else:
        print("You have 5 lives.")
    return (size, lives)

if __name__ == '__main__' :
    dictionary = import_dictionary(dictionary_file)
    print("Welcome to the Hangman Game")
    (size,lives) = get_game_options()
    danger = 0
    response = "Y"
    while response == "Y":
        waah = choice(dictionary[size])
        wpp = []
        for k in range(size):
            wpp.append("__")
        for tyt in range(len(waah)):
            if waah[tyt] == "-":
                wpp[tyt] = "-"
        danger = 0
        eu = []
        while lives >= 0:
            if "__" not in wpp:
                print("You guessed right!")
            print("Letters chosen: ",end="")
            print(','.join(eu))
            print((' ').join(wpp), end= ' ')
            print(f'lives: {lives}', end=" ")
            ww = []
            wp =[]
            for bhaii in range(danger):
                ww.append("X")
            for poo in range(lives):
                wp.append("O")
            print(''.join(ww),end='')
            print(''.join(wp))
            if "__" not in wpp:
                print(f'Congratulations!!! You won! The word is {waah}!')
                break
            if lives ==0:
                print(f'You lost! The word is {waah}!')
                break
            okk = input("Please choose a new letter > ")
            if okk not in eu:
                eu.append(okk)
            else:
                print("You have already chosen this letter.")
            if okk not in waah:
                lives -= 1
                danger += 1
                print("You guessed wrong, you lost one life.")
            elif okk in waah:
                for kj in range(len(waah)):
                    if waah[kj] == okk:
                        wpp[kj] = okk
        response = input("Would you like to play again [Y/N]? ")
        if response != "Y":
            break
        (size,lives) = get_game_options()
    print("Goodbye!")
            