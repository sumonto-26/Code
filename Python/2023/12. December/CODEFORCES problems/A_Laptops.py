# DATE --> 26 December 2023

ans = 'Poor Alex'
for i in range(int(input())):
    a = list(map(int,input().split(" ")))
    if a[0] < a[1]:
        ans = 'Happy Alex'
print(ans)