n = int (input())
a = list(map(int, input().split(" ")))
m = min(a)
c = 0
for i in a: 
    if i % m == 0: 
        c+=1
print(m if c==n else '-1')