# Time ==> 11:18 - 11:28
# Date ==> 10 January 2024
# time_complexity ==> 92 ms
n = int(input())
a = input()
c1 = a.count("1")
c2 = a.count("2")
c3 = a.count("3")
m = max([c1, c2, c3])
print(n-m)