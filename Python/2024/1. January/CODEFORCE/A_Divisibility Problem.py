# Date --> 14 January 2024
for _ in range(int(input())):
    a = list(map(int,input().split(" ")))
    if a[0] % a[1] == 0:
        print("0")
    else:
        print(a[1]-(a[0] % a[1]))