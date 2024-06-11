# DATE == 11 JUNE 2024
# AUTHOR == SUMONTO
for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int,input().split()), reverse=True)
    is_find = False
    for i in range(n-2):
        if a[i] == a[i+1] and a[i] == a[i+2]:
            print(a[i])
            is_find = True
            break
    if is_find != True:
        print(-1)