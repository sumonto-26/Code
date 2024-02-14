# Date--> 17 December 2023

a = list(map(int, input().split(" ")))
k = a[0] 
n = a[1] 
w = a[2] 

b = [i*k for i in range(1, w+1)]

ans = sum(b) - n
if ans < 0 :
    print('0')
else:
    print(ans)

