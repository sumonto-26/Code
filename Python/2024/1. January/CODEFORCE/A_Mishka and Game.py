# DATE--> 6 January 2023
m = []
c = []
for _ in range(int(input())):
    a = list(map(int,input().split(" ")))
    if a[0] > a[1] :
        m.append(a[0])
    elif a[1] > a[0]:
        c.append(a[1])

if len(m) > len(c): print("Mishka")
elif len(c) > len(m) : print("Chris")
else: print("Friendship is magic!^^")