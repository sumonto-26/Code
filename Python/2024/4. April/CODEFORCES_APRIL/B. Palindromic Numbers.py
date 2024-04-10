def solve(a):
    last_digit = a % 10
    if last_digit == 9:
        ans1 = int('1' * (len(str(a)) + 1))
    else:
        ans1 = int('9' * len(str(a)))
    print(ans1 - a)
        

for _ in range(int(input())):
    digit = int(input())
    a = int(input())
    solve(a)
    
# not compelite not compelite not compelite not compelite
# not compelite not compelite not compelite not compelite
# not compelite not compelite not compelite not compelite
# not compelite not compelite not compelite not compelite
# not compelite not compelite not compelite not compelite
# not compelite not compelite not compelite not compelite
# not compelite not compelite not compelite not compelite
# not compelite not compelite not compelite not compelite
# not compelite not compelite not compelite not compelite
# not compelite not compelite not compelite not compelite
# not compelite not compelite not compelite not compelite
# not compelite not compelite not compelite not compelite