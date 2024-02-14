# DATE 26 December 2023
# my logic

a = int(input())
b = sorted(map(int, input().split()))

c = sum(b) / 2
n = []
current_sum = 0

for value in reversed(b):
    if current_sum <= c:
        n.append(value)
        current_sum += value
    else:
        break

print(len(n))


# other's logic 

n = int(input())
a = list(map(int, input().split()))
 
x = 0
y = sum(a)
 
a.sort(reverse = True)
for i in range(n):
    x += a[i]
    y -= a[i]
 
    if x > y:
        print(i+1)
        break
 
