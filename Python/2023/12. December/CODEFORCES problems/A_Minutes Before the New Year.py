for _ in range(int(input())):
    a = list(map(int,input().split(" ")))
    h = a[0]*60
    m = h + a[1]
    print(1440 - m)
