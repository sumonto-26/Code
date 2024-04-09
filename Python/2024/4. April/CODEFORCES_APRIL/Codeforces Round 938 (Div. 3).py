# Authour ==> SUMONTO, AGE ==> 15y;
# A. Yogurt Sale
"""for _ in range(int(input())):
    a = list(map(int,input().split(" ")))
    n = a[0]
    ans1 = n*a[1]
    ans2 = ((n-1)*a[2])+a[1]
    
    if a[1]*2 < a[2]:
        print(ans1)
    else:
        if n % 2 == 0:
            print((n//2)*a[2])
        else:
            print((((n-1)//2)*a[2])+a[1])
"""


"""for _ in range(int(input())):
    n, c, d = map(int, input().split())
    ans = "YES"
    x = sorted(map(int, input().split()))
    matrix = [x[i*n:(i+1)*n] for i in range(n)]
    for i in matrix:
        print(i)
    print(matrix)"""
    
"""for _ in range(int(input())):
    n, c, d = map(int, input().split(" "))
    x = list(map(int,input().split(" ")))
    m = []
    demo = [j for j in range(min(x),n*c, c)]
    for i in range(1,n):"""
    
def solve (n, a_11, c, d, x):
    arr = []
    cur_ele = a_11
    
    for i in range(n):
        for j in range(n):
            arr.append(cur_ele)
            cur_ele += c
        a_11 += d
        cur_ele = a_11
    
    if sorted(arr) == sorted(x):
        return "YES"
    else:
        return "NO"

# Example values
for _ in range(int(input())):
    n, c, d = map(int, input().split(" "))
    x = list(map(int,input().split(" ")))

    # Print the progressive square
    ans = solve(n, min(x), c, d, x)
    print(ans)
