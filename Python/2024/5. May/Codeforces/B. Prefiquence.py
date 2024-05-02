for _ in range(int(input())):
    N = list(map(int,input().split()))
    a = input()
    b = input()
    ans = 0
    j = 0
    for i in range(max(N)):
        if i<N[1] and j<N[0]:
            if a[j] == b[i]:
                ans += 1
                j += 1
        else:
            break
        
    print(ans)
    print()