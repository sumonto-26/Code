# DATE --> 3 January 2024
# TIME -->  6:35 - 7:30
# TIME COMPLEXITY --> 46ms # is the best time for python
# ACCEPTED in 3rd try
# RATING --> 1000
# my logic
a = input()
if "1"in a:
    start = a.index("1")
    a = a[start:]
z = a.count('0')
o = a.count('1')
if z >= 6 and o >= 1:   print("yes")
else: print("no")


'''
# TIME COMPLEXITY --> 46ms # is the best time for python
# aayushi04's LOGIC !!!!
n = str(input())
n = (n.lstrip("0"))
#print(n)
if n.count("0") >=6 and len(n)>=7:
    print("yes")
else:
    print("no")
'''