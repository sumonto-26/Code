# DATE ==> 20 AUGUST 2024
# AUTHOR ==> SUMONTO

'''
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    max_count = 0
    max_count_num = 0
    for i in set(arr):
        if arr.count(i)>max_count:
            max_count = arr.count(i)
            max_count_num = i
    print(n-max_count)
'''

for _ in range(int(input())):
    n = int(input())
    if n%2 == 0: print(-1)
    else: 
        p1 = 1
        p2 = n
        for i in range(n):
            if i%2 == 0: 
                print(p2, end = " ")
                p2 -= 1
            else:  
                print(p1, end = " ")
                p1 += 1
        print()
