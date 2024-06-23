# DATE ==> 23 June 2024
# AUTHOR ==> SUMONTO

import math
n,m = map(int,input().split())
if n<m: print(-1)
else:
    if n%2 == 0:
        start = n//2
        end = n
        for i in range(start, end+1):
            if i%m == 0: 
                print(i)
                break
    else:
        start = math.ceil(n/2)
        end = n
        for i in range(start, end+1):
            if i%m == 0: 
                print(i)
                break
    