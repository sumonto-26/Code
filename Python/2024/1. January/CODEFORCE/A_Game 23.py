# DATE --> 3 January 2024
# TIME -->  7:10 - 7:49
# TIME COMPLEXITY --> 46ms # best time complexity #
# ACCEPTED in 2nd try
# RATING --> 1000
# my logic

a = list(map(int,input().split(" ")))
n = 0
if a[0]==a[1]:
    print("0")
elif a[1] % a[0] != 0 :
    print('-1')
else:
    while True:
        if a[1] % (a[0]*2) == 0:
            a[0] = a[0] * 2
            n += 1
        elif a[1] % (a[0]*3) == 0:
            a[0] = a[0]*3 
            n += 1
        elif a[0] == a[1]:
            print(n)
            break
        else:
            print("-1")
            break

