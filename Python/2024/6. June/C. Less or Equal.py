# DATE ==> 9 JUNE 2024
# AUTHOR ==> SUMONTO

n = list(map(int,input().split()))
a = sorted(map(int,input().split()))
b = a[:n[1]]
a = a[n[1]:]
if n[1] == 0:
    print(min(a)-1 if min(a)-1 > 0 else -1)
elif a.count(max(b))>=1:
    print(-1)
else: 
    print(max(b))
