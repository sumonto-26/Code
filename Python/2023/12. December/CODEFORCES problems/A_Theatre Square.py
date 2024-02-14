# Date--> 15 december 2023
import math

a = list(map(int, input().split(" ")))
a1,a2,a3 = a[0],a[1],a[2]
b = a1 / a3
b1 = a2 / a3

c = math.ceil(b)
c1 = math.ceil(b1)
ans = c * c1

print(ans)
