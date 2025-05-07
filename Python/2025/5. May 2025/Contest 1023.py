"""import math
from functools import reduce

def compute_gcd(arr):
    return reduce(math.gcd, arr)

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    found = False

    for i in range(n):
        B = [a[i]]
        C = a[:i] + a[i+1:]

        if len(C) > 0 and compute_gcd(B) != compute_gcd(C):
            print("YES")
            # Output 1 for B, 2 for C
            result = []
            for j in range(n):
                result.append(1 if j == i else 2)
            print(*result)
            found = True
            break

    if not found:
        print("NO")"""


for _ in range(int(input())):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    max_ = max(arr)
    min_ = min(arr)
    counter = arr.count(max_)
    if(max_-min_ > k+1 or (max_-min_ >= k+1 and counter > 1)):
        print("Jerry")
    else: print("Jerry" if sum(arr)%2 == 0 else "Tom")
        