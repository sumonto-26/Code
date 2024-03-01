# DATE ==> 29 February 2024
# RATING ==> 800
# TIME COMPLEXITY ==> 31ms
# MY LOGIC.

def find_answer(n, a):
    c = 0
    if a in n:
        for i in range(n.count(a)):
            if n.index(a) % 2 == 0:
                c += 1
                
            else:
                n = n.replace(a, "_", 1)
                
    print("YES" if c != 0 else "NO")

for _ in range(int(input())):
    n = input()
    a = input()
    find_answer(n, a)
    
