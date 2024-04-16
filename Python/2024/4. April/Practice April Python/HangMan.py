import random
List = ["programming", "Python", "coding", "django" ]

word = random.choice(List)
lenght = len(word)
blanks = list("_" * lenght)
life = 6

print("_  " * lenght)

while True:
    a = input("\nEnter a letter: ")
    if a in word:
        for i in range(lenght):
            if a == word[i]:
                blanks[i] = a
    else:
        life -= 1
        print(f"\nLife == {life} !!!")
        
    print()
    for j in blanks:
        print(j, end ="  ")
    print()
        
    
    if "_" not in blanks:
        print("\n!!!!!!!!!!!!!!!! YOU WIN !!!!!!!!!!!!!!!!\n")
        break
    if life == 0:
        print("\n!YOU LOSE!\n")
        break
    