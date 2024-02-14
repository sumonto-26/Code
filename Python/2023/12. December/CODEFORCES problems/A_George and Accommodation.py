n = 0
for i in range(int(input())):
    a = list(map(int, input().split(' ')))
    if a[1]-a[0] >= 2:
        n += 1
print(n)
