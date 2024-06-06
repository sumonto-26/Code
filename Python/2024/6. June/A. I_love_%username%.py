# DATE ==> 6/June/2024
# AUTHOR ==> SUMONTO

n = int(input())
arr = list(map(int,input().split()))
ans = 0
for i in range(1,n):
    if arr[i]>max(arr[:i]) or arr[i]<min(arr[:i]):
        ans += 1
print(ans) 