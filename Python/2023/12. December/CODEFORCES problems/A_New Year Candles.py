a = list(map(int,input().split(' ')))
n = []
a1 = a[0]

if a[0] < a[1]:
    print(a[0])

else:
    while True:
        a[0] = a[0] / a[1]
        n.append(a[0])
        if a[0] < a[1]:
            break
    
    i = sum(n) + a1
    j = round(i)

    if i > j :  print(j+1)
    else:   print(j)