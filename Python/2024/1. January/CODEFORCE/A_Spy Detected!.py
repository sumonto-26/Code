# Date ==> 15 January 2024
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split(" ")))
    a2 = list(set(a))
    x = a.count(a2[0])
    y = a.count(a2[1])
    if x > y:
        print(a.index(a2[1])+1)
    if x < y:
        print(a.index(a2[0])+1)