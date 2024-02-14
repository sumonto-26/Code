for i in range(int(input())):
    a = int(input())
    b = list(map(int,input().split(" ")))
    ans = max(b) - min(b)
    print(ans)