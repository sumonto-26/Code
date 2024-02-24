def solve():
    l = []
    for _ in range(n):
        a = list(map(int,input()))
        l.append(sum(a))
    return l
for _ in range(int(input())):
    n = int(input())
    ans = solve()
    if ans.count(max(ans)) == max(ans):
        print("SQUARE")
    else:
        print("TRIANGLE")
    
            