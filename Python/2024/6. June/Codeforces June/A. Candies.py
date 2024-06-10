# DATE ==> 10 JUNE 2024
# AUTHOR ==> SUMONTO

for _ in range(int(input())):
    n = int(input())
    x = 1
    for i in range(1,int(n**0.5)+1):
        x = (x*2)+1
        if n % x == 0:
            print(n//x)
            break
