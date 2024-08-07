# DATE ==> 6 AUGUST 2024
# AUTHOR ==> SUMONTO
'''
for _ in range(int(input())):
    a = input()
    print(int(a[0])+int(a[1]))
'''

'''
for _ in range(int(input())):
    a1,a2,b1,b2 = list(map(int,input().split()))
    ans = 0
    if a1 > b1 and a2 > b2: ans += 1
    if a2 > b2 and a1 > b1: ans += 1
    if a2 > b1 and a1 > b2: ans += 1
    if a1 > b2 and a2 > b1: ans += 1
    print(ans) 
'''


'''
for _ in range(int(input())):
    a = list(map(int,input().split()))
    arr = []
    l = r = 0
    for i in range(a[0]):
        l1,r1 = map(int,input().split())
        arr.append(l1-r)
        l = l1
        r = r1
        if i == a[0]-1: arr.append(a[2]-r1)
    print("YES" if max(arr) >= a[1] else "NO")
'''

for _ in range(int(input())):
    a = input()
    b = input()
    i = j = 0
    while(i<len(a) and j<len(b)):
        if a[i] == b[j]:
            i+=1
            j+=1
        elif a[i] == "?":
            a = list(a)
            a[i] = b[i]
            a = "".join(a)
            i+=1
            j+=1
        else: 
            print("NO")
            break
    
    else: 
        print("YES")
        a = a.replace("?", "a")
        print(b+a)