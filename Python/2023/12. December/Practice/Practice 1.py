import random 
print(" \nWelcome to this game in this game you type a number and this number has a value head or tall\n")
a = int(input("Enter a seed number: "))
random.seed(a)
r = random.randint(0,1)
n = random.randint(0,1)
user1 = "You Head" if r == 0 else "You Tall"
ai = "AI Tall" if n == 0 else "AI Tall"

print(f'\n{user1} and {ai}')