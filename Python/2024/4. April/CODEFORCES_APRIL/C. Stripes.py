for _ in range(int(input())):
    l = []
    for _ in range(8):
        a = list(map(str,input()))
        l.append(set(a))
    if {'R'} in l:
        print("R")
    else:
        print("B")