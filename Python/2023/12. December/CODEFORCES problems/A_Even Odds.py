a = list(map(int,input().split(" ")))

n = a[0]/2
if a[0] % 2 == 0:
    if a[1] <= n:
        s = a[1] + (a[1]-1)
        print(round(s))
    else:
        s = (a[1]-n) * 2
        print(round(s))

if a[0] % 2 != 0:
    if a[1] <= n + 1:
        s = a[1] + (a[1]-1)
        print(round(s))
    else:
        s = (a[1]-n) * 2
        print(round(s-1))

# good logic

# n, k = map(int, input().split())
# if k <= n-n//2:
#     print(2*k-1)
# else:
#     k -= n-n//2
#     print(2*k)