# Date --> 1 | 1 | 2023

a = input()
s = a[1:-1]
a1 = set(map(str,s.split(', ') ))
ans = len(a1)
print('0' if a == '{}' else ans)
    