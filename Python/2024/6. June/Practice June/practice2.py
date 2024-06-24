
def solve(n):
    m = ((n*n)+n)//2
    ans = []
    for i in range(m-n+1, m+1):
        ans.append(i)
    return ans

n = int(input())
print(solve(n))
for i in range(1,11):
    print(solve(i))
    print(sum(solve(i)),"-------", ((i*i*i)+i)//2)
    