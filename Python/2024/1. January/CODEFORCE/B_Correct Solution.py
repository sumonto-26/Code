for _ in range(int(input())):
    a = int(input())
    s = set()
    for j in str(a):
        if j != '0':
            s.add(j)
    s = "".join(sorted(s))
    
    for i in s:
        a_copy = a 
    
        while a_copy % int(i) != 0:
            a_copy += 1
        
    print(a, a_copy)


# not conpelite
# not conpelite
# not conpelite
# not conpelite
# not conpelite
# not conpelite
# not conpelite
# not conpelite
# not conpelite
# not conpelite