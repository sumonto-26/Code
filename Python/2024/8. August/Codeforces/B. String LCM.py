# AUTHOR ==> SUMONTO DATTA
# DATE == 22 AUGUST 2024 
# PROBLEM NAME ==> B. String LCM
# PROBLEM RATING ==> 1000
# PROBLEM TOPICS ==> Brute Force, Math, Number Theory, Strings.

import math
for _ in range(int(input())):
    a = input()
    b = input()
    if min(len(a),len(b)) == 0: print(-1)
    else:
        n = math.lcm(len(a),len(b))
        a = a*(n//len(a))
        b = b*(n//len(b))
        if a == b: print(a)
        else: print(-1)