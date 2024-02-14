# Date --> 7 January 2023
# TIME --> 10:07 - 10:25am
for _ in range(int(input())):
    n = []
    a = input()
    s = 'abcdefgh'
    a1 = a[0]
    a2 = a[1]
    for i in range(8):
        if a1+str(i+1) != a: 
            n.append(a1+str(i+1))
        if s[i] + a2 != a :
            n.append(s[i] + a2 )
    ans = ' '.join(n)
    print(ans)