# DATE ==> 25 JULY 2024
# AUTHOR ==> SUMONTO
for _ in range(int(input())):
    n = int(input())
    print("YES" if n&(n-1) != 0 else "NO")