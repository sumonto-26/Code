def is_palindrome(h, m):
    return f"{h:02}:{m:02}" == f"{h:02}:{m:02}"[::-1]

def solve(h, m, x):
    seen = set()
    count = 0
    for _ in range(1440): 
        time_key = h * 60 + m
        if time_key in seen:
            break
        seen.add(time_key)
        if is_palindrome(h, m):
            count += 1
        total = h * 60 + m + x
        h = (total // 60) % 24
        m = total % 60
    return count


for _ in range(int(input())):
    s = input()
    d = int(s[6:])
    h,m = int(s[:2]), int(s[3:5])
    print(solve(h,m,d))
    