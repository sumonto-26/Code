a = list(map(str, input().split(" ")))
a1 = int(a[0])
a2 = int(a[1])

for i in range (a2):
    if a1 % 10 == 0:
        a1 = a1 / 10
    else:
        a1 = a1 - 1

print(int(a1))