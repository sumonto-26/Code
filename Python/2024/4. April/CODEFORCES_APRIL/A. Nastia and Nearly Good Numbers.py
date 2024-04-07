for _ in range(int(input())):
    a,b = map(int,input().split(" "))
    n1 = a+(a*b)
    g = (a*b)*b
    n2 = g-n1
    if b != 1:
        print("YES")
        print(F"{n1} {n2} {g}")
    else:
        print("NO")