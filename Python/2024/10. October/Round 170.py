# DATE ==> 14 October 2024
# AUTHOR ==> SUMONTO
for _ in range(int(input())):
    ans = 0
    s = input()+" "
    t = input()+" "
    n = len(s)-1
    m = len(t)-1
    for i in range(min(n, m)):
        if(s[i] == t[i]): ans += 1;
        else:     break
    n -= ans
    m -= ans
    if(ans > 0): ans += 1;
    ans += n+m
    print(ans)