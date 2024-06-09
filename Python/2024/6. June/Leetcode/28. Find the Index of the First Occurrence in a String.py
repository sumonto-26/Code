# DATE ==> 9 JUNE 2024
# AUTHOR ==> SUMONTO

haystack = input()
needle = input()

if needle not in haystack:
    print(-1)
else:
    n = len(needle)
    if n == 1:
        if needle in haystack: 
            print(haystack.index(needle))
    else:
        for i in range(n, len(haystack)+1):
            #print(haystack[i-n:i])
            if haystack[i-n:i] == needle:
                print(i-n)