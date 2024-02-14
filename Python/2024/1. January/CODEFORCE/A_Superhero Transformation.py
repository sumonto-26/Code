# DATE --> 5 January 2024
# TIME COMPLEXITY --> 62ms 
# ACCEPTED in 4th try
# RATING --> 1000
# my logic
import re
a = input()
b = input()
c = re.sub("[aeiou]", "a", a)
d = re.sub("[aeiou]", "a", b)
x = re.sub("[bcdfghjklmnpqrstvwxyz]", "b", c)
y = re.sub("[bcdfghjklmnpqrstvwxyz]", "b", d)
print("YES" if x == y else "NO")

# Raghul_A.S's logic
# TIME COMPLEXITIY --> 31 ms
'''s=input()
t=input() 
m=len(s) 
n=len(t) 
if m!=n:
   print("NO") 
else:
   for i in range (m) :
       if (s[i] in 'aeiou' and t[i] in 'aeiou') or (s[i]  not in 'aeiou' and t[i] not in 'aeiou') :
          continue
       else:
           print ("NO")
           break 
 
   else:
         print ("YES")'''