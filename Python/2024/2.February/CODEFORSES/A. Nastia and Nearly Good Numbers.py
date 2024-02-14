# Date 9 February 2024
def ans(a, b):
    c = a * b

    for i in range(1, 100):
        n = c * i
        if a * i != (n - (a * i)) and a * i % b != 0 and (n - (a * i)) % b != 0:
            print("YES")
            print(a * i, (n - (a * i)), (a * i) + (n - (a * i)))
            return
        
    for i in range(1, 100):
        n = c * i
        if b * i != (n - (b * i)) and b * i % a != 0 and (n - (b * i)) % a != 0:
            print("YES")
            print(b * i, (n - (b * i)), (b * i) + (n - (b * i)))
            return
    print("NO") 

for _ in range(int(input())):
    a, b = map(int, input().split())
    ans(a, b)

# not compelite
# not compelite
# not compelite
# not compelite
# not compelite
# not compelite
# not compelite
# not compelite
# not compelite