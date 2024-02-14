# Date ==> 18 January 2024

a = list(map(int, input().split(" ")))
ans1 = a[0] - a[1]
ans2 = a[0] - a[2]

if ans1 < ans2:
    print(ans1)
else:
    print(ans2)