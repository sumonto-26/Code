# DATE ==> 10 JUNE 2024
# AUTHOR ==> SUMONTO
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    print(" ".join(map(str,sorted(a)[::-1])))