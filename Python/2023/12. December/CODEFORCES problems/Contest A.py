# for i in range(int(input())):
#     b = sorted(map(int,input().split(' ')))
#     print(b[1])

# B

# for i in range (int(input())):
#     a = int(input())
#     b = sorted(input())
#     l = 'abcdefghijklmnopqrstuvwxyz'
#     ans = l.index(b[-1])
#     print(ans +1)

# C

for _ in range(int(input())):
    a = int(input())
    b = list(map(int, input().split(' ')))
    m = max(b)
    
    s = sorted(b)
    second_max = s[-2] if len(s) > 1 else m

    n = [str(m - second_max) if x == m else str(x - m) for x in b]
    
    ans = ' '.join(n)
    print(ans)

