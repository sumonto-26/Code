# A

# for i in range(int(input())):
#     a = int(input())
#     b = sorted(input())
#     c = sorted("Timur")
#     if b == ['T', 'i', 'm', 'r', 'u']:
#         print("YES")
#     else:
#         print("NO")

# B
import re
for _ in range(int(input())):
    a = int(input())
    b = input()
    c = input()
    x = re.sub('G',"B",b)
    y = re.sub('G',"B",c)
    print("YES" if x == y else "NO")

