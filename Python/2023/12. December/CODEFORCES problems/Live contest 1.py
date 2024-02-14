# A 
for i in range(int(input())):
    a = list(map(str,input().split(' ')))
    if a[0]==a[1]:
        print(a[2])
    elif a[0]==a[2]:
        print(a[1])
    else:
        print(a[0])

