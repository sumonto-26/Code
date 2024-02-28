for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split(" "))) 
    for i in range(n):
        a[i] = abs(a[i])
    print(sum(a))