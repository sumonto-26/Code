def divisors(num):
    dl = []
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            dl.append(i)
            if num // i != i:
                dl.append(num // i)
    return sorted(dl)[-2:]

for _ in range(int(input())):
    a = list(map(int,input().split(" ")))
    x = a[0]
    y = a[1]
    ans = y*2
    divisor = sum(divisors(ans))
    print(divisor, a) 
    while divisor != sum(a):
        if divisor > sum(a) :
            ans += y
        else:
            ans += y
    print(ans)
    
    
# not compelite
# not compelite
# not compelite
# not compelite
# not compelite
# not compelite
# not compelite
# not compelite