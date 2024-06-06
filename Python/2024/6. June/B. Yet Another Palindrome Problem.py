# DATE ==> 6/June/2024
# AUTHOR ==> SUMONTO
# PROBLEM RATING ==> 1100
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    is_palindrome = False
    for i in range(n):
        for j in range(i+2, n): 
            if arr[i] == arr[j]: is_palindrome = True
    print("YES" if is_palindrome else "NO")
            