for _ in range(int(input())):
    a = int(input())
    b = input()
    a1 = b.count('A')
    b1 = b.count('B')
    if a1 > b1:
        print("A")
    else:
        print("B")