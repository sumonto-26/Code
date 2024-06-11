# DATE ==> 10 JUNE 2024
# AUTHOR ==> SUMONTO
import math
def is_fair(n):
    lcm_ = 1
    for i in set(str(n)):
        if i!= "0":
            lcm_ = math.lcm(lcm_, int(i))
    return (n%lcm_ == 0)
        
for _ in range(int(input())):
    n = int(input())
    while(is_fair(n) != True):
        n += 1
    print(n)

            