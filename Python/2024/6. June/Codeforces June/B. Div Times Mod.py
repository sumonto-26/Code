# DATE ==> 26 JUNE 2024
# AUTHOR ==> SUMONTO

# We know that,  (x div k)⋅(xmodk)=n

import math
n,k = map(int,input().split())
x = n
while 1:
    if math.floor((x/k))*(x%k) == n:
        print(x)
        break
    x += 1
    
# TIME ERROR # TIME ERROR # TIME ERROR
# TIME ERROR # TIME ERROR # TIME ERROR
# TIME ERROR # TIME ERROR # TIME ERROR
# TIME ERROR # TIME ERROR # TIME ERROR
# TIME ERROR # TIME ERROR # TIME ERROR