n = input()
if int(n) >= 0:
    print(n)
elif len(n) == 3 and n[-1] == "0" and n[0] == "-":
        print("0")
else:
    n1 = n[:-1]
    n2 = n.replace(n[-2], "")
    if int(n1) < int(n2):
        print(n2)
    else:
        print(n1)
        
# not complite
# not complite
# not complite
# not complite
# not complite
# not complite
# not complite
# not complite
# not complite
# not complite