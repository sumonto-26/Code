# DATE ==> 29 February 2024
# RATING ==> 800
# TIME COMPLEXITY ==> 46ms
# MY LOGIC.
s = input()
a = s.count("a")
if a > len(s)//2:
    print(len(s))
else:
    print((a*2)-1)