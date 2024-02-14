# DATE --> 7 January 2023
# 3:00 - 3:11
# my logic
a = list(map(int, input().split(" ")))
n = []
ans = "NO"
for _ in range(a[1]):
    b = list(map(int, input().split(" ")))
    n.append(b)
for i in sorted(n):
    if a[0] > i[0] :
        a[0] += i[1]
        ans = "YES"
    elif a[0] <= i[0]: ans = "NO"
    
print(ans)

