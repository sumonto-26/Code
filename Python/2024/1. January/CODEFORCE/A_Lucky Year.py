# 14 January 2024
a = int(input())
if a <=9:
    print("1")
else:
    a = str(a)
    c = len(a)-1
    n = str(int(a[0])+1) + ("0"*c)
    ans = int(n) - int(a)
    print(ans)