for _ in range(int(input())):
    s1=0
    s2=0
    s=0
    n = int(input())
    a = list(map(int,input().split(" ")))
    if len(a)==1:
        if int(a[0])<2:
            print('YES')
        else:
            print('NO')
    else:
        for i in range(len(a)):
            if i%2==0:
                s1+=a[i]
            else:
                s2+=a[i]
        if s1-s2 == 0 or s1-s2 == -1 or s1-s2==1:
            print('YES')
        else:
            print('NO')