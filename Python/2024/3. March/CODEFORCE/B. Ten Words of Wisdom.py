# B. Ten Words of Wisdom 
for _ in range(int(input())):
    l = []
    l2 = []
    for i in range(int(input())):
        a = list(map(int,input().split(" ")))
        l2.append(a)
        if a[0] <= 10:
            l.append(a)
            
    ans = max(l, key=lambda x: x[1])
    ans2 = l2.index(max(l, key=lambda x: x[1]))
    print(ans2 + 1)