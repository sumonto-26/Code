# DATE ==> 13 JUNE 2024
# AUTHOR ==> SUMONTO

def find_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if n // i != i:
                divisors.append(n // i)
    return divisors

def find_pow(a, b, l):
    ans = 1
    n = min(a, b)
    while n < l:
        n *= min(a, b)
        ans += 1
    return min(10, ans)

num_cases = int(input())
for _ in range(num_cases):
    a, b, l = map(int, input().split())
    ks = set() 
    n = find_pow(a, b, l)
    divs = find_divisors(l)

    powers_a = [a**x for x in range(n + 1)]
    powers_b = [b**y for y in range(n + 1)]

    for k in divs:
        found = False
        for x in range(n + 1):
            if found: break
            for y in range(n + 1):
                if k * powers_a[x] * powers_b[y] == l:
                    ks.add(k)
                    found = True
                    break
            if found: break
    print(len(ks))

# TIME ERROR # TIME ERROR # TIME ERROR 
# TIME ERROR # TIME ERROR # TIME ERROR 
# TIME ERROR # TIME ERROR # TIME ERROR 
# TIME ERROR # TIME ERROR # TIME ERROR 
# TIME ERROR # TIME ERROR # TIME ERROR 
# TIME ERROR # TIME ERROR # TIME ERROR 

