#DATE 24 January 2024

import math
a = list(map(int,input().split(" ")))
m = a[1]
b = list(map(int,input().split(" ")))
n = []
for i in range(a[0]):
    e = math.ceil(b[i]/m)
    n.append(e)
    
    
for j in range(len(n)-1, -1, -1):
    if n[j] == max(n):
        print(j+1, n)
        break