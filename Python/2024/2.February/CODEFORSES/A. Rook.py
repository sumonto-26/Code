for _ in range(int(input())):
    a = input()
    s = "abcdefgh"
    for i in range(1,9):
        ans1 = a[0]+str(i)
        ans2 = str(s[i-1]) + a[1]
        if ans1 != a:
            print(ans1)
        if ans2 != a:
            print(ans2)