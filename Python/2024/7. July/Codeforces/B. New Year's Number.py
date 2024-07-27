# DATE ==> 27 JULY 2024
# TIME ==> 12:22 PM
# AUTHOR ==> SUMONTO

import math

def solve(n):
    if n< 2020: return "NO"
    for i in range(math.ceil(n/2020)+1):
        if (n-(i*2020))%2021 == 0: return "YES"
    return "NO"
    
for i in range(int(input())):
    n = int(input())
    print(solve(n))