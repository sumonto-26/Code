#DATE ==> 9 May 2024
# AUTUOR ==> SUMONTO
n = int(input())
arr =  sorted(map(int,input().split()))
if sum(arr[:n]) == sum(arr[n:]):
    print(-1)
else:
    for i in arr:
        print(i, end=" ")
