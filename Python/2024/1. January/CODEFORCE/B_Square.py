for _ in range(int(input())*2):
    a = list(map(int,input().split(" ")))
    b = list(map(int,input().split(" ")))

    if a[0] == b[0]:    ans = "YES" if a[1] / 2 == b[1] else "NO"
    elif a[1] == b[1]:  ans = "YES" if a[0] / 2 == b[0] else "NO"
    elif a[1] == b[0]:  ans = "YES" if a[0] / 2 == b[1] else "NO"
    elif a[0] == b[1]:  ans = "YES" if a[1] / 2 == b[0] else "NO"
    
    print(ans)

# NOT CORRECT ANSWER
# NOT CORRECT ANSWER
# NOT CORRECT ANSWER
# NOT CORRECT ANSWER
# NOT CORRECT ANSWER
# NOT CORRECT ANSWER
# NOT CORRECT ANSWER
# NOT CORRECT ANSWER
# NOT CORRECT ANSWER
# NOT CORRECT ANSWER