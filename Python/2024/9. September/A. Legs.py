# DATE ==> 4 September 2024
# AUTHOR ==> SUMONTO
# PROBLEM NAME ==> A. Legs
# CONTEST NAME ==>  Codeforces Round 962 (Div. 3)
# Link ==> https://codeforces.com/problemset/problem/1996/A
# PROBLEM RATING ==> 800
# PROBLEM TAGS ==> Binary Search, Math, Ternary Search.
# Time Limit Per Test ==> 2 Second.
# Memory Limit Per Test ==> 256 MegaBytes.
"""
It's another beautiful day on Farmer John's farm.
After Farmer John arrived at his farm, he counted n
legs. It is known only chickens and cows live on the farm, and a chicken has 2 legs while a cow has 4.
What is the minimum number of animals Farmer John can have on his farm assuming he counted the legs of all animals?
"""

import math
for _ in range(int(input())):
    n = int(input())
    print(math.ceil(n/4))        