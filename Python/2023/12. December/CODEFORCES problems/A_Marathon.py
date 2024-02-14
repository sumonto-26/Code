# Date --> 17 December 2023

a = int(input())
n = []
for i in range(a):
    b = list(map(int, input().split(" ")))
    for j in range(len(b)):
        if b[0]<b[j]:
            n.append(b[j])

    print(len(n))
    n.clear()

