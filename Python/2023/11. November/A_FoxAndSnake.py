v, m = map(int, input().split())

s1 = "#"*m
s2 = "."*(m-1)+'#'
s3 = "#"+"."*(m-1)
s = [s1,s2,s1,s3]
for i in range(v):
    print(s[i%4])
    print(i%4)



'''

for i in range(1,m+1):
    if i%2 == 1: print('#'*n)
    elif i%2 == 0 and i % 4 == 0:print('#'+'.'*(n-1))
    else:print('.'*(n-1) + '#') 

'''