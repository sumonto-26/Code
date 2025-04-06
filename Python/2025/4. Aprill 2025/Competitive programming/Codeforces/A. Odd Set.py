for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    odd = 0
    for i in arr:
        if i%2 == 1: odd += 1
    print("YES" if odd == n else "NO")