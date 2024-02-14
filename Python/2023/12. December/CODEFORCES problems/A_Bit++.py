# 2 December 2023
# nijer thika # In myself it's my logic
a = int(input())
b = 0
for i in range(a):
    c = input()
    if c == "X++"or c == "++X":
        b = b + 1
    else:
        b -= 1
print(b) 
