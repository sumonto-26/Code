# DATE ==> 1 March 2024
# RATING ==> ?
# TIME COMPLEXITY ==> 46ms
# MY LOGIC.

for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split(" ")))
    i = a[0]
    j = a[-2]
    k = a[1]
    l = a[-1]
    print((abs(i - j)) + (abs(j - k)) + (abs(k - l)) + (abs(l - i)))

