# Date ==> 29 January 2024
def divisor(n):   
    ans = 0
    for i in range(3,int(n**0.5)+1,2):
        if n % i == 0:
            ans += 1
            break
    if ans == 0:
        print("NO")
    else:
        print("YES")
        
for _ in range(int(input())):
    n = int(input())
    if n % 2 != 0:
        print("YES")
    else:    
        divisor(n)
        
        
'''
# Time Error # Time Error 
# Time Error # Time Error 
# Time Error # Time Error 
# Time Error # Time Error 
# Time Error # Time Error 
# Time Error # Time Error 
# Time Error # Time Error''' 
    