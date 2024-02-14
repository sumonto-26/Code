# DATE--> 20 December 2023

a = list(map(int, input().split(" ")))
s = str(a[1])
if a[0] < len(s):
    print('-1')

elif a[1] == 10:
    n = a[0]-1
    zeros = n * '0'
    print(F'1{zeros}')

else:   print(a[0]* s)