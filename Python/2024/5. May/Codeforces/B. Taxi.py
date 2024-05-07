# DATE ==> 7 May 2024
# AUTHOR ==> SUMONTO
import math

n = int(input())
arr = list(map(int, input().split()))    
a = arr.count(1)
b = arr.count(2)
c = arr.count(3)
ans = arr.count(4)

while a>0 and c>0:  
    a -= 1
    c -= 1
    ans += 1
    
    if c > 0:
        ans += c
        c = 0
        
    if a > 0:
        ans+= math.floor(a/4)
        if a%4 != 0:
            ans += 1
            print(ans)
            a = 0
    
    if b > 0:
        ans += math.floor(b/2)
        if b%2 != 0:
            ans += 1
            b = 0
            
print(ans)

# Wrong code # Wrong code # Wrong code 
# Wrong code # Wrong code # Wrong code 
# Wrong code # Wrong code # Wrong code 
# Wrong code # Wrong code # Wrong code 


