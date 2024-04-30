"""def is_correct(a,b):
    for i in range(len(a)):
        if a[i] > b[i]:
            return False
    else:
        return True

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    a = sorted(a)
    b = list(map(int,input().split()))
    b = sorted(b)
    ans = 0
    while (is_correct(a,b) == False):
        for i in range(n):
            a = sorted(a)
            if (a[i] > b[i]):
                a.append(b[i])
                a.remove(max(a))
                ans += 1
    else:
        print(ans)
    """

# B
for _ in range(int(input())):
    n = int(input())
    a = input()
    print("NO" if ((a.count("U"))%2==0) else "YES")