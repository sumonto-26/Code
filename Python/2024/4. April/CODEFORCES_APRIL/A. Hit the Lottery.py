a = int(input())
money = [100, 20, 10, 5, 1]

ans = 0
for i in money:
    ans += a // i
    a %= i

print(ans)

# Best Code
"""n = int(input())
a1 = (n // 100)
a2 = (n % 100 // 20)
a3 = (n % 20 // 10)
a4 = (n % 10 // 5)
a5 = (n % 5//1)
print(a1+a2+a3+a4+a5)"""