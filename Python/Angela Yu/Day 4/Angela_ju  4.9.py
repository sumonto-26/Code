import random

rock = '''

    _______
---'   ____)
      (______)
      (______)
      (_____)
---'__(___)
      
'''

paper = '''
    _______
---'   ____)____
       _________)
       __________)
       _________)
---.__________)

'''

scissors = '''
    _______
---'   ____)____
           _____)
      ___________)
      (_____)
---.__(___)
      
'''

game_Drawings = [rock, paper, scissors]

user_choice = int(input("What do you choice? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
print('\n Your choice: ')
print(game_Drawings[user_choice])


computer_choice = random.randint (0, 2)
print("Computer_choice:")
print(game_Drawings[computer_choice])

    
# if user type INVALIS NUMBERS
if user_choice >= 3 or user_choice < 0:
    print("YOU TYPE AN INVALIS NUMBER, YOU LOSE!")
    
# draw
elif computer_choice == user_choice:
    print("IT'S A DRAW")
    
elif user_choice == 0 and computer_choice == 2:
    print("YOU WINS !")

elif computer_choice == 0 and user_choice == 2:
    print("YOU LOSE !")
    
elif computer_choice > user_choice:
    print("YOU LOSE !")
    
elif user_choice > computer_choice:
    print("YOU WINS !")