for _ in range(int(input())):
    a = int(input())
    n = 0
    while a >= 2:
        if a % 6 == 0:
            a /= 6
            n += 1
        else:
            a *= 2
            n += 1
            if a % 6 != 0:
                n = -1
                break
    print(n)