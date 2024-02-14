n = int(input())
a = input()
s = set(a)
for i in s:
    c = a.count(i)
    if len(s) % n != 0 and c % n == 0:
        print('-1')
        break
    else:
        s = "".join(s)
        ans = s*n
        print(ans)
        break
    
    
# Not compelit
# Not compelit
# Not compelit
# Not compelit
# Not compelit
# Not compelit
# Not compelit
# Not compelit
# Not compelit
# Not compelit
# Not compelit
# Not compelit