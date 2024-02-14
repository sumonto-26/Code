a = int(input())
condition = "NO"
if a % 4 == 0 or a % 7 == 0 or a % 47 == 0 or a % 74 == 0 or a % 447 == 0 or a % 774 == 0 or a%477 ==0:
    condition = "YES"

print(condition)