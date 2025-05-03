# DATE =====> 3 May 2025
# AUTHOR =====> SUMONTO
# PROBLRM =====> https://codeforces.com/problemset/problem/451/B

n = int(input())
arr = list(map(int,input().split()))
s_arr = sorted(arr)
a = 0
b = 0

for i in range(len(arr)-1):
    if arr[i]>=arr[i+1]:
        a = i
        break
    
for i in range(1,len(arr)):
    if arr[i-1]>=arr[i]:
        b = i
        

arr = arr[:a]+(arr[a:b+1][::-1])+arr[b+1:]
if (arr == s_arr):
    print("yes")
    print(a+1, b+1)
    
else: print("no")