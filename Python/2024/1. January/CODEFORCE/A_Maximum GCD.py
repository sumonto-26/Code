'''import math
    
def factor(a):
    n = []
    for i in range(1, int(a**0.5)+1):
        if a % i == 0:
            n.append(i)   
            if a // i != i:
                n.append(a//i)
    return n

p = []
a = [i for i in range(1,3001)]
divisors = sorted(factor(a))

for d in divisors:
    if len(factor(d)) == 2:
        p.append(d)

c = len(p)
lis = []
print(divisors)
if c == 2:
    lis.append(a)'''
    
    
def factor(a):
    n = []
    for i in range(1, int(a**0.5)+1):
        if a % i == 0:
            n.append(i)   
            if a // i != i:
                n.append(a//i)
    return n
    
n = int(input())
factors = factor(n)
ans = 0
answer = []
empty = []
divisors = [[] for _ in range(3001)]

for d in range(1, 3001):
    for a in range(d, 3001, d):
        divisors[a].append(d)
    
    if len(divisors[d]) == 2:
        empty.append(d)
        
for i in factors:
    if i in empty:
        ans += 1
        
if ans == 2:
    answer.append(n)
else:
    pass

print(answer)

