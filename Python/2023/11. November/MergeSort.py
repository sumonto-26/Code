a = int(input())
b1 = list(map(int,input().split(" ")))
b = sorted(b1)
c = sum(b)/2
n = []
while sum(n) < c:
    for i in range(0,len(b)):
        if sum(n) <= c:
            n.append(b[-i])

print(len(n), n)