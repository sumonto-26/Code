# DATE ==> 28 February 2024
# RATING ==> 1500
# Time Complexity ==> 62ms
# My Logic .
a = input()
b = a
ans = 0

if "AB" in b :
    b = b.replace("AB", " ", 1)
    if "BA" in b :
        ans += 1

if "BA" in a :
    a = a.replace("BA", " ", 1)
    if "AB" in a :
        ans += 1

if ans != 0:
    print("YES")
else:
    print("NO")
    

# Other's Logic
# Time Complexity ==> 46ms
"""
s=input()
a=s.count("AB")
b=s.count("BA")
c=s.count("ABA")
d=s.count("BAB")
if(a*b==c+d or a==0 or b==0):
    print("NO")
else:
    print("YES")"""