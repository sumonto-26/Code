a = int(input())
n = a
for _ in range(a):
    b = input()
    if b.isalpha() == True :
        n -= 1
    elif int(b) < 18:
        n -= 1
    

print(n)