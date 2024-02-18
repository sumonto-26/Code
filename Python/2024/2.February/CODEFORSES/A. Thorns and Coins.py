def solve(n , a):
    ans = 0
    if "**" in a:
        a = a[:a.index("**")]
        return a.count("@")
    else:
        return a.count("@")
                
for _ in range(int(input())):
    n = int(input())
    a = input()
    ans = solve(n, a)
    
    print(ans)