n = int(input())

cnt = 0
for i in range(1, int(n**0.5) + 1):
    if n % i == 0:
        cnt += 1

        if i != n // i:
            cnt += 1

print(cnt)
