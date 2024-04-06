l = []
for _ in range(int(input())):
    a = sum(map(int,input().split(' ')))
    l.append(a)
print(max(l))