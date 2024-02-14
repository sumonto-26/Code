# Date --> 15 December 2023 
# //////my logic/////
# submit at 11:25 AM accepted in second try

# b = [1 if "-." in a[:2]  2 elif "--" in a[:2] else 0] //wrong answer//
# b = [n.append('1') if "-." in a[:2] else n.append('2')  if "--" in a[:2] else n.append('0')]

n = list(map(str, input().split()))

if '--' in n[0]:
    n[0] = n[0].replace('--', '2')

if "-." in n[0]:
    n[0] = n[0].replace('-.', '1')

if "." in n[0]:
    n[0] = n[0].replace('.', '0')

ans = ''.join(n)
print(ans)