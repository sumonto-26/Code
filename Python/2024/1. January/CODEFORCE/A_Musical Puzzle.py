for _ in range(int(input())):
    n = int(input())
    a = input()
    l = []
    for i in range(n-1):
        s = a[i:i+2]
        if s in l:
            pass
        else:
            l.append(s)
    print(len(l))