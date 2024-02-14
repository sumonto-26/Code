# DATE --> 5 January 2024
# TIME COMPLEXITY --> 46ms 
# ACCEPTED in 1st try
# RATING --> 900
# my logic
zero = []
one = []
for _ in range(int(input())):
    a = list(map(int,input().split(" ")))
    zero.append(a[0])
    one.append(a[1])
if zero == one:
    if zero[::-1] == sorted (zero):  print("maybe")
    else:  print("unrated")
else:   print("rated")

# vishu.ut's code
# TIME COMPLEXITIY --> 46ms
'''
w=int(input())
l=[]
flag=0
for i in range(w):
    t=list(map(int,input().split()))
    if t[0]!=t[1]:
        flag=1
    else:
        l.append(t[0])
if flag!=1:
    y=list(l)
    y.sort(reverse=True)
    if y==l:
        print('maybe')
    else:
        print('unrated')
else:
    print('rated')'''