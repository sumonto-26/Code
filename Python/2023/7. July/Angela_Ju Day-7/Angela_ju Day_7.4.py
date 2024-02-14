#Step 1

word_list = ["ardvark", "baboon", "camel"]

# TODO_1 - Randomly choose a word
# from the word_list and assign it 
# to a variable called chosen_word.
import random
chosen_word =  random.choice(word_list)

# TODO_2 - Ask the user to guess a 
# letter and assign their answer to 
# a variable called guess. Make
# gess lowercase. 
guess = input("Guess a letter: ").lower()

# TODO_3 - Check if the letter the
# user guessed (guess) is one of the 
# letters in the chosen_word.
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")