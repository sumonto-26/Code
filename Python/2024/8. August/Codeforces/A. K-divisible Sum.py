# AUTHOR ==> SUMONTO DATTA
# DATE == 22 AUGUST 2024 
# PROBLEM NAME ==> A. K-divisible Sum
# PROBLEM RATING ==> 1000
# PROBLEM TOPICS ==> Binary Search, Constructive Algorithms, Greedy, Math.

import math
for _ in range(int(input())):
    n,k = map(int, input().split())
    i = math.ceil(n/k)
    x = (k*i)-n
    answer = math.ceil(x/n)+1
    print(answer)