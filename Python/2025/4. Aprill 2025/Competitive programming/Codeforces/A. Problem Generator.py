for _ in range(int(input())):
    n,m = map(int, input().split())
    s = input()
    x = 0
    s1 = "ABCDEFG"
    for i in s1: 
        x += min(m,s.count(i))
    print((7*m) - x)
    