n = int(input())

ans = []
x = list(map(int,input().split(" ")))
y = list(map(int,input().split(" ")))
z = x[1:] + y[1:]
if len(set(z)) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")