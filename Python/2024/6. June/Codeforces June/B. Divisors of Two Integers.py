# DATE ==> 12 JUNE 2024
# AUTHOR ==> SUMONTO

def find_div(num):
    divisors = []
    for i in range(1,int(num**0.5)+1):
        if num%i == 0: 
            divisors.append(i)
            if num//i != i:
                divisors.append(num//i)
    return sorted(divisors)

n = int(input())
d = list(map(int,input().split()))

x = max(d)
divs = find_div(x)

ans = []
for i in range(n):
    if d.count(d[i]) == 2 or d[i] not in divs:
        ans.append(d[i])
        

print(x, max(ans))
