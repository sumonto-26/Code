# DATE ==> 3 May 2024
# AUTHOR ==> SUMONTO.

for _ in range(int(input())):
    n = int(input())
    s = str(n)
    if n % 7 == 0:
        print(n)
    else:
        ans = 0
        for i in range(len(s) - 1, -1, -1):
            for j in range(10):
                copy_s = list(s)
                copy_s[i] = str(j)
                new_n = int(''.join(copy_s)) # List to int
                if new_n % 7 == 0:
                    ans = new_n
                    break
            if ans!= 0:
                print(ans)
                break

