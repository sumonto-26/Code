# A Lucky
"""
for _ in range(int(input())):
    a = list(map(int,input()))
    if a[0]+a[1]+a[2] == a[3]+a[4]+a[5]:
        print("YES")
    else:
        print("NO")
"""


# B. Equal Candies
"""for _ in range(int(input())):
    n = int(input() )
    a = list(map(int,input().split(" ")))
    ans = sum(a) - (n*min(a))
    print(ans)"""
    
# C. Most Similar Words
def solve():
    for _ in range(int(input())):
        n, m = map(int, input().split())  
        strings = [input() for _ in range(n)]  
        ans = float('inf') 
        for i in range(n - 1):
            for j in range(i + 1, n):
                sum_ = 0
                for k in range(m):
                    dis = abs(ord(strings[i][k]) - ord(strings[j][k]))
                    sum_ += dis
                ans = min(ans, sum_)
        print(ans)

solve()

