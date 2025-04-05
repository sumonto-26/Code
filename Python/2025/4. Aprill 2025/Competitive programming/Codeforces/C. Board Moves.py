for _ in range(int(input())):
    n = int(input())
    ans = 0
    a = 0
    for i in range(1,n+2,2):
        x = (2*i)+((i-2)*2)
        ans += x*a
        a+=1
    print(ans)