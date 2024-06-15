# DATE ==> 15 JUNE 2024
# AUTHOR ==> SUMONTO

def find_divisors(n):
    divs = []
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            divs.append(i)
            if n//i != i: divs.append(n//i) 
    return sorted(divs)

def find_pair(n):
    common_divisors = find_divisors(n)
    for d in common_divisors:
        if n % d == 0:
            return (n//d,  n//d * (d - 1))
    return (1, n-1)

for _ in range(int(input())):
    n = int(input())
    x, y = find_pair(n)
    print(x, y)

