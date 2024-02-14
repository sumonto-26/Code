a = int(input())

for abcd in range(a):
    b = input()

    if len(b)>10:
        c = len(b)-2
        print(f"{b[0]}{c}{b[-1]}")

    else:
        print(b)
