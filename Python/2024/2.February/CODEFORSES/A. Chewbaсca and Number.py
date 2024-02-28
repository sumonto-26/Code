# Date ==> 28 February 2024
# Rating ==> 1200
# Time Complexity ==> 46ms
# My Logic
a = input()        
f = a[0]
if f == '9' or int(f) < 5:
    for i in range(1,len(a)):
        if int(a[i]) >= 5:
            a = a.replace(a[i], str(9-int(a[i])))
    print(f+a[1:])
    
else:
    for i in range(len(a)):
        if int(a[i]) >= 5:
            a = a.replace(a[i], str(9-int(a[i])))
    print(a)
    
# Other's Logic 
# Time Complexity ==> 31ms
'''
n=int(input())
s=str(n)
t=''
for i in range(len(s)):
    if i!=0 or s[i]<'9':
        t+=min(s[i],str(9-int(s[i])))
    else:
        t+=s[i]
print(t)
'''