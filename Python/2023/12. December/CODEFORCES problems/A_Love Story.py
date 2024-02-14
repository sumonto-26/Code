# DATE 18 December 2023
# My logic 31ms

for _ in range(int(input())):
    a = input()
    n = 0
    c = 'codeforces'
    for i in range (0,10):
        if a[i] != c[i]:
            n += 1
    print(n)

# Other's logic 30ms BUT WHY?

# t=int(input())
# for i in range(t):
#     s=str(input())
#     g="codeforces"
#     c=0
#     for j in range(len(s)):
#         if s[j]!=g[j]:
#             c+=1
#     print(c)