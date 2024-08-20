# DATE ==> 19 AUGUST 2024
# TIME ==> 1:58PM - 2:45PM
# PROBLEM NAME ==> E. Building an Aquarium
# PROBLEM TAGS ==> Binary Search, Sortings
# PROBLEM RATING ==> 1100
# AUTHOR ==> SUMONTO

def find_water(walls, height):
    answer = 0
    walls = [min(i,height) for i in walls]
    for i in walls:
        answer += height-i
    return answer

for test_cast in range(int(input())):
    lenght, water = list(map(int,input().split()))
    walls = list(map(int,input().split()))
    
    find_water(walls, 5)
    minimum,maximum = 0, water+max(walls)
    while(minimum <= maximum):
        middle = int(minimum/2 + maximum/2)
        if(find_water(walls, middle) <= water and find_water(walls,middle+1) > water):
            print(middle)
            break
        elif(find_water(walls, middle) < water): minimum = middle+1
        else: maximum = middle-1
    