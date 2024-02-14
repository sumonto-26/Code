# Date 30 January 2024
for _ in range(int(input())):
    a = list(map(int,input().split(" ")))
    n = a[0] // 1
    m = a[1] // 2
    if n == 0:
        print(f"-{m}")
    elif m == 0:
        print(f"-{n}")
    else:
        print(n*m)