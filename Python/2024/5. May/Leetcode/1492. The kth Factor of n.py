# Date ==> 4 May 2024
# AUTHOR ==> SUMONTO

n = int(input())
k = int(input())
factors = []
for i in range(1,int(n**0.5)+1):
    if n%i == 0:
        factors.append(i)
        factors.append(n//i)
factors = sorted(set(factors))
ans = factors[k-1]
print(ans)