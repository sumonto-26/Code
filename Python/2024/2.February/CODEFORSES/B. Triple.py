def solve(n, a):
    s = set(n)
    
    if len(s) >= a:
        print('-1')
    
    else:
        for i in s:
            if n.count(i) >= 3:
                print(i)
                break
        else:
            print("-1")

for _ in range(int(input())):
    a = int(input())
    n = list(map(int,input().split(" ")))
    solve(n, a)
    
    
    # Time Error  # Time Error  # Time Error  # Time Error
    # Time Error  # Time Error  # Time Error  # Time Error
    # Time Error  # Time Error  # Time Error  # Time Error
    # Time Error  # Time Error  # Time Error  # Time Error
    # Time Error  # Time Error  # Time Error  # Time Error
    # Time Error  # Time Error  # Time Error  # Time Error
    # Time Error  # Time Error  # Time Error  # Time Error
    # Time Error  # Time Error  # Time Error  # Time Error
    # Time Error  # Time Error  # Time Error  # Time Error
    # Time Error  # Time Error  # Time Error  # Time Error
    # Time Error  # Time Error  # Time Error  # Time Error
    # Time Error  # Time Error  # Time Error  # Time Error