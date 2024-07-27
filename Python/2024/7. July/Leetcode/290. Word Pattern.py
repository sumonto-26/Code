# DATE ==> 27 JULY 2024
# TIME ==> 7:44 AM
# AUTHOR ==> SUMONTO

pattern = input()
s = input()
a = list(s.split(" "))
b = list(pattern)

if len(a) != len(b): print(False)
else:
    n = 0
    for i in range(len(a)):
        if a.index(a[i]) == b.index(b[i]):
            n += 1
            # print(a.index(a[i]), b.index(b[i]))
    print(n == len(pattern))