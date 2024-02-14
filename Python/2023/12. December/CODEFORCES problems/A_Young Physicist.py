x = []
y = []
z = []
for _ in range(int(input())):
    
    b = list(map(int,input().split(" ")))
    x.append(b[0])
    y.append(b[1])
    z.append(b[2])

print("YES" if sum(x) == 0 and sum(y) == 0 and sum(z) == 0 else "NO")


n = []
x = [] 
for _ in range(int(input())):
    b = list(map(int,input().split(" ")))
    x.append(b[0])
    for i in b: 
        n.append(i)

print("YES" if sum(n) == 0 and sum(x) == 0 else "NO")