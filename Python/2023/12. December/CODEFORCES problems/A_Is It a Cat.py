import re
for _ in range(int(input())):
    a = int(input())
    b = input().lower()
    b = re.sub(r"(.)\1*", r"\1", b)
    ans = ''.join(b)
    print("YES" if ans == 'meow' else "NO")