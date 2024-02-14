# Date 8 February 2024
# my logic
for _ in range(int(input())):
    a = int(input())
    if a <= 1:
        print("-1")
    else:
        ans = "2" + "3" * (a-1)
        print(ans)
