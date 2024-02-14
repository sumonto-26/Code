# DATE --> 3 January 2024
# TIME --> 6:40-6:55
# ACCEPTED in 1st try

# my logic
import re
a = int(input())
b = int(input())
c = a + b
n = re.sub('0', "", str(c))
a1 = re.sub('0', "", str(a))
b1 = re.sub('0', "", str(b))
c1 = str(int(a1) + int(b1))
print("YES" if n == c1 else "NO")

"""
# Other's logic by doctorsmurger 
# he's logic is same my logic

a = input()
b = input()
c = int(a)+int(b)
c = str(c)
a1 = a.replace('0', '')
b1 = b.replace('0', '')
c1 = c.replace('0', '')
if int(a1)+int(b1) == int(c1):
    print('YES')
else:
    print('NO')"""