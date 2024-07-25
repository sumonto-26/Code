# DATE ==> 25 JULY 2024
# AUTHOR ==> SUMONTO

# Method ==> 1
for _ in range(int(input())):
    n = int(input())
    print("YES" if n&(n-1) != 0 else "NO")

# Method ==> 2
for _ in range(int(input())):
    n = int(input())
    if (n%2 != 0): print("YES")
    else:
        while n > 1:
            n = n/2
        print("YES" if n!=1 else "NO")