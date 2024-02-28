# DATE ==> 28 February 2024
# RATING ==> 800
# TIME COMPLEXITY ==> 46ms
# MY LOGIC.
a = input()
n = list(map(int, input().split(" ")))
s = set(n)
ans = []
for i in s:
    ans.append(n.count(i))
print(max(ans)) 