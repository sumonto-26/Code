# Date --> 1 | 1 | 2023
# My Logic

x = int(input())
y = sorted(map(int,input().split(" ")))
s = sum(y)
if s % 2 == 0:
    print(s)
else:
    ind = 0
    while True:
        ans = s- y[ind]
        if ans % 2 == 0:
            print(ans)
            break
        else:
            ind += 1



# Other's Logic

# input()
# a=list(map(int,input().split()))
# s=sum(a)
# if(s%2==0):
#     print(s)
# else:
#     s -= min(i for i in a if i%2)
#     print(s)
