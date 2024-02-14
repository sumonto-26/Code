# Date ---> 3 January 2024

for _ in range(int(input())):
    a = int(input())
    b = list(map(int,input().split(" ")))
    if len(b) == len(set(b)):
        print("YES")
    else:
        print("NO")