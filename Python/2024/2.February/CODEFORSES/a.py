for _ in range(int(input())):
    n = int(input())
    a = input()
    i = 0
    c = a.count("B")
    if c == 1:
        print("1")
    else:
        s = a.index("B")
        a = a[::-1]
        e = a.index("B")
        e = (n-e)
        ans = a[s:e]
        print(len(ans))
        