def solve():
    n = int(input("Lenght of array "))
    a = list(map(int, input("Sorted Array ").split(" ")))

    x = int(input("LowerBound of "))

    l = 0 
    r = n - 1
    ans = -1

    while l <= r:
        m = (l + r) // 2
        
        if a[m] < x:
            l = m + 1
        else:
            ans = a[m]
            r = m - 1

    print(ans) # Lowerbound

solve()
