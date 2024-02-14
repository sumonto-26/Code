# Date ==> 10 January 2024
# problem rating ==> 900
# Time Complexity ==> 545ms
# my_logic
n = int(input())
m = int(input())
ans = m % (2**n)
print(ans)



# Kashem_1234567's code
# Time Complexity ==> 31ms
'''
n = int(input())
m = int(input())
if n>30:
    print(m)
else:
    print(m%(2**n))'''