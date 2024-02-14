# Date --> 25 December 2023 
# //////my logic/////

a = list(map(int,input().split(" ")))
n = '#Black&White'
for i in range(a[0]):
    b = list(map(str,input().split(" ")))
    if "C" in b or 'M' in b or "Y" in b:
        n = '#Color'
print(n)

