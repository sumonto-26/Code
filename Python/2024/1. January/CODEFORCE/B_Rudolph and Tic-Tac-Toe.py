# DATE --> 3 January 2024
# TIME --> 09:51 - 10:30am
# TIME COMPLEXITY --> 108ms 
# ACCEPTED in 2nd try
# RATING --> 1000

# my logic
for _ in range(int(input())):
    a = input()
    b = input()
    c = input()
    if (a[0] == 'X'and b[0] == "X" and c[0] == "X" or
    a[1] == "X" and b[1] == "X" and c[1] == "X" or 
    a[2] == "X" and b[2] == "X" and c[2] == "X" or
    a[0] == "X" and b[1] == "X" and c[2] == "X" or 
    a[2] == "X" and b[1] == "X" and c[0] == "X" or 
    a == "XXX" or b == "XXX" or c == "XXX"):
        print("X")

    elif (a[0] == 'O'and b[0] == "O" and c[0] == "O" or
    a[1] == "O" and b[1] == "O" and c[1] == "O" or 
    a[2] == "O" and b[2] == "O" and c[2] == "O" or
    a[0] == "O" and b[1] == "O" and c[2] == "O" or 
    a[2] == "O" and b[1] == "O" and c[0] == "O" or 
    a == "OOO" or b == "OOO" or c == "OOO"):
        print("O")

    elif (a[0] == '+'and b[0] == "+" and c[0] == "+" or
    a[1] == "+" and b[1] == "+" and c[1] == "+" or 
    a[2] == "+" and b[2] == "+" and c[2] == "+" or
    a[0] == "+" and b[1] == "+" and c[2] == "+" or 
    a[2] == "+" and b[1] == "+" and c[0] == "+" or 
    a == "+++" or b == "+++" or c == "+++"):
        print("+")

    else: print("DRAW")

# Viserion7's logic
# TIME COMPLEXITY --> 46ms
'''
import sys
for i in range(int(input())):
    r1 = sys.stdin.readline().rstrip()
    r2 = sys.stdin.readline().rstrip()
    r3 = sys.stdin.readline().rstrip()
    if r1[0]==r1[1]==r1[2] and "." not in r1:
        print(r1[0])
    elif r2[0]==r2[1]==r2[2] and "." not in r2:
        print(r2[0])
    elif r3[0]==r3[1]==r3[2] and "." not in r3:
        print(r3[0])
    elif r1[0]==r2[0]==r3[0] and r1[0]!=".":
        print(r1[0])
    elif r1[1]==r2[1]==r3[1] and r1[1]!=".":
        print(r1[1])
    elif r1[2]==r2[2]==r3[2] and r1[2]!=".":
        print(r1[2])
    elif r1[0]==r2[1]==r3[2] and r1[0]!=".":
        print(r1[0])
    elif r1[2]==r2[1]==r3[0] and r1[2]!=".":
        print(r1[2])
    else:
        print("DRAW")'''