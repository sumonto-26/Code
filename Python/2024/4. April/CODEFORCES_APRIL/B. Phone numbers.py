a = int(input())
n = input()
for i in range(a-2, 1, -2): 
    n = n[:i] + "-" + n[i:]
print(n)
