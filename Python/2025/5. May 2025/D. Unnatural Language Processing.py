# DATE -----> 4 May 2025
# AUTHOR -----> SUMONTO
# PROBLEM -----> https://codeforces.com/contest/1915/problem/D

for _ in range(int(input())):
    n = int(input())
    s = input()
    i = 0
    result = []

    while i < n:
        result.append(s[i])
        if i <= n - 3 and s[i] in 'ae':
            if s[i+2] in 'ae':
                result.append('.')
                result.append(s[i+1])
                i += 2
            else:
                result.append(s[i+1])
                result.append('.')
                result.append(s[i+2])
                i += 3
        else: i+=1

    print(''.join(result))
