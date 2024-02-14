#for _ in range(int(input())):
#    a = input()
#    if a == "abc" or a == "acb" or a == "bac" or a == "cba":
#        print("YES")
#    else:
#        print("NO")

# b
'''
for _ in range(int(input())):
    b = int(input())
    a = list(map(int,input().split(" ")))
    m = a.index(min(a))
    a[m] = min(a)+1
    ans = 1
    for i in range(b):
        ans = ans* a[i]
    print(ans)'''
    
