# DATE ==> 17 JUNE 2024
# AUTHOR ==> SUMONTO

import math

def divide(a, b):
    y = 0
    while a != 0:
        a = math.floor(a / b)
        y += 1
    return y

for _ in range(int(input())):
    a, b = map(int, input().split())
    minimum_way = 1000
    
    if b == 1:
        b += 1
        minimum_way = divide(a, b) + 1
        for x in range(1, 70):
            y = divide(a, b + x )
            if minimum_way > x + y+1:
                minimum_way = x + y+1
        
    else:
        if a < b: 
            minimum_way = 1
        if a == b: 
            minimum_way = 2
        minimum_way = divide(a, b)
        for x in range(1, 70):
            y = divide(a, b + x )
            if minimum_way > x + y:
                minimum_way = x + y
        
    print(minimum_way)
