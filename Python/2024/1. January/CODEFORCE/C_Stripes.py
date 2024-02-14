n = ''
for i in range(int(input())):
    for j in range(8):
        b = input()
        s = len(set(b))
        n += f'{b} {s}'
        print(n)

    if 'RRRRRRRR' in n :
        if '.' in b :
            s -= 1
            print("B" if '2' in s else "R")
        else:
            print("R")
    
        print("B")

    n = ''

# NOT COMPELITE
# NOT COMPELITE
# NOT COMPELITE
# NOT COMPELITE
# NOT COMPELITE
# NOT COMPELITE
# NOT COMPELITE
