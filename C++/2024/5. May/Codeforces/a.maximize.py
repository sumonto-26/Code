import math

for _ in range(int(input())):
    x = int(input())
    arr = []
    for i in range(1,x):
        arr.append(math.gcd(x,i)+i)
    ind = arr.index(max(arr))
    print(ind+1)
    