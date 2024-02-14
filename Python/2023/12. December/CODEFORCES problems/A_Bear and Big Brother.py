# DATE --> 15 December 2023
a = list(map(int, input().split(" ")))

n = 0
while True:
    n += 1
    a[0] = a[0] * 3
    a[1] = a[1] * 2
    if a[0] > a[1]:
        break

print(n)
