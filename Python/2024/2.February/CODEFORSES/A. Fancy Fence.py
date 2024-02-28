# Date ==> 27 February 2024
# Rating 1100
# My Logic
# Time Complexity ==> 154ms
for _ in range(int(input())):
    ans = [round((i-2)*180 / i, 4)  for i in range(3, 400)]
    a = int(input())
    a = round(a, 4)
    if a in ans :
        print("YES")
    else:
        print("NO")
        
# Other's logic
# Time Complexity ==> 30ms
'''t = int(input())
for _ in range(t):
    a = int(input())
    if 360 % (180 - a) == 0:
        print("YES")
    else:
        print("NO")'''