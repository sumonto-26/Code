a = input()
u,l = 0,0

for i in a:
    if i.isupper():
        u += 1
    else:
        l += 1

if u <= l :
    print(a.lower())
else:
    print(a.upper())

