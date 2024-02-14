def find_lcm(x, y):
    # Find the greater number
    greater = max(x, y)
    
    while True:
        if greater % x == 0 and greater % y == 0:
            lcm = greater
            break
        greater += 1
    
    return lcm



for _ in range(int(input())):
    x = []
    y = []
    ans = []
    a = int(input())
    for i in range(1,a):
        x.append(i)
    y = list(reversed(x))
    f = find_lcm(x[0],y[0])
    r = x[0]
    e = y[0]
    for i in range(len(x)):
        t = find_lcm(x[i],y[i])
        if t < f:
            r = x[i]
            e = y[i]
            f = t
    print(f'{r} {e}')
    
# not compelite
# not compelite
# not compelite
# not compelite
# not compelite
# not compelite
# not compelite
# not compelite
# not compelite
# not compelite
# not compelite
# not compelite
# not compelite
# not compelite
# not compelite
# not compelite