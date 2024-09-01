# DATE ==> 1 September 2024
# CONTEST ==> Codeforces Round 970 (Div. 3)
# AUTHOR  ==> SUMONTO

# Problem A
# Problem Name ==> A. Sakurako's Exam
'''
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a % 2 == 1 or (a == 0 and b % 2 == 1): print("NO")
    else:  print("YES")
'''

# Problem B
# Problem Name ==> B. Square or Not
# import math
# for _ in range(int(input())):
#     n = int(input())
#     s = input() 
#     if(int(math.sqrt(n)) == math.sqrt(n)):
#         a = '1' * int(math.sqrt(n))
#         ans = a
#         b = '1' + '0'*(int(math.sqrt(n))-2) + '1'
#         for i in range(int(math.sqrt(n))-2):
#             ans += b
#         ans += a
#         print("Yes" if ans == s else "No")
#     else: print("No")   

# Problem C
# Problem Name ==> C. Longest Good Array
for _ in range(int(input())):
    l,r = map(int,input().split())
    start, end, ans =  0, 1000000, 1
    while(start <= end):
        mid = int(start+(end-start)/2)
        if((l+(mid*(mid+1))/2) <= r): 
            ans = mid
            start = mid+1
        else: end = mid-1
        # print(mid)
        
    print(ans+1)