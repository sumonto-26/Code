a,b = input().split(" ")
n = []
for i in range(len(a)+1):
    s = list(reversed(sorted(a[:i])))
    s = "".join(s)
    if a[:i] == s:
        ans = a[:i]
print(ans + b[0] )

