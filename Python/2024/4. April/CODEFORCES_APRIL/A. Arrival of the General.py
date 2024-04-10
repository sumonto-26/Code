# DATE ==> 10 April 2024
# Author ==> Sumonto
n = int(input())
a = list(map(int, input().split()))
ans = 0

# Sorting the first element to its correct position
while a[0] != max(a):
    max_index = a.index(max(a))
    for i in range(max_index, 0, -1):
        a[i], a[i-1] = a[i-1], a[i]
        ans += 1

# Sorting the last element to its correct position
while a[-1] != min(a):
    min_index = len(a) - 1 - a[::-1].index(min(a))
    for i in range(min_index, len(a)-1):
        a[i], a[i+1] = a[i+1], a[i]
        ans += 1
print(ans)
