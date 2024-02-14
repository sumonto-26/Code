# Date --> 14 December 2023 
# //////my logic/////
# submit at 8:35 PM -- 9:25 accepted in first try

a = int(input ())
n = 0 

b = list(map(int, input().split(" ")))
for i in range(0 , len(b)):
    n += b[i]

d = n / a
print(round(d, ndigits = 12))