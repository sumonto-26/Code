for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split(" ")))
    ind = 0
    l = 0
    for i in range(n):
        x = a[ind]
        y = a[ind+1]
        z = min(x, y)
        l += z
        ind += 1
    print(l)