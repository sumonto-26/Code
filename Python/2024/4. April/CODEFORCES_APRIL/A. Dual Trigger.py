for _ in range(int(input())):
    a = int(input())
    s = input()
    one = s.count("1")
    if one>1:
        ind = s.index('1')
    if one == 2:
        if s[ind] == s[ind+1]:
            print("NO")
        else:
            print("YES")
            
    elif one % 2 == 0 and a > 2 and one > 2 or one == 0:
        print("YES")
    else:
        print("NO")