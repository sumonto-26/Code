# TIME --> 5:00 - 5:36pm
# Date --> 6 january 2023
# Rating --> 1100
# TIME COMPLEXITY --> 46ms
# My Logic
a = list(map(int,input().split(" ")))
c = 0 
for _ in range(a[0]):
    k = sorted(set(map(str,input())))
    ans = "".join(k)
    n = ''
    for i in range(a[1]+1):  n += str(i)
    if n in ans :  c += 1
print(c)


# RimRaider9's Logic
# TIME COMPLEXITY --> 31ms
'''
n,k=map(int,input().split())
count=0
for i in range(n):
  num=input()
  if k==0:
    num=num[1:]
  if len([i for i in list(range(k+1)) if i not in sorted(set(map(int,num)))])==0:
    count+=1
print(count)'''