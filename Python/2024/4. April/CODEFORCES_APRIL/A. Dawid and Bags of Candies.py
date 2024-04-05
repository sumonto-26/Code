a = sorted(map(int,input().split(' ')))
if (a[0] + a[-1]) == (a[1] + a[2]):
    print("YES")
elif (a[-1]) == sum(a)-a[-1]:
    print("YES")
else:
    print("NO")