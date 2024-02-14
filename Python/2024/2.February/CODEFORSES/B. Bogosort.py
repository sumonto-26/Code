import random

def ans(a, n):
    random.shuffle(a)
    for i in range(n-1):
        if i - int(a[i]) != i+1 - int(a[i+1]):
            answer = " ".join(a)
            print(answer)
            break

for _ in range(int(input())):
    n = int(input())
    a = list(map(str,input().split(" ")))
    ans(a,n)