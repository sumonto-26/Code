# Date --> 14 December 2023 
# //////my logic/////
# submit at 6:26 PM accepted in first try

a = int(input())
for i in range(a):
    b = input()
    n = len(b)
    if n % 2 != 0: 
        print("NO")
    else:
        if  b[: n//2] == b[n//2:]:
            print("YES")
        else:
            print("NO")

