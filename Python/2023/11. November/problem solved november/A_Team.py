a = int(input())

d = 0

for i in range(a):

    b = input()
    c0 = str(b).count("0")
    c1 = str(b).count("1")
    if c0 < c1:
        d += 1

print(d)
    
    