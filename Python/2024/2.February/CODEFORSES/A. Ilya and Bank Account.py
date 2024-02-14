a = int(input())
if a > 0:
    print(a)
else:
    at = str(a)
    sa = sorted(at)[::-1]
    for i in range(len(at)):
        n = sa.count(sa[i])
        if n >= 2 and sa[i] != min(sa):
            m = at.index(sa[i])
            at = at[::-1].replace(at[m], '', 1)
            print(at[::-1])
            break
    else:
        m = max(at)
        ans = at.replace(m,'',1)
        print('0' if ans == '-0' else ans)
            
        
# error error error
# error error error
# error error error
# error error error
# error error error
# error error error
# error error error
# error error error
# error error error