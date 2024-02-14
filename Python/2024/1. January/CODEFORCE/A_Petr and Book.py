# DATE --> 3 January 2024
# TIME -->  7:10 - 7:49
# TIME COMPLEXITY --> 1278ms 
# RATING --> 1000
# my logic
a = int(input())
n = list(map(int,input().split(" ")))
ans = 0

while True:
    if sum(n) < a:
        n += n
    if sum(n[: ans]) >= a:
        break
    else:
        ans += 1
while ans > 7:
    ans -= 7
print(ans)


# Pravallika_Gundubilli
# TIME COMPLEXITY --> 62ms 

'''
n=int(input())
a=list(map(int,input().split(" ")))
c=0
while(c<n):
   for i in range(7):
        c+=a[i]
        if c>=n:
            print(i+1)
            break
 '''