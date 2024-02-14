# Date ==> 18 January 2023
a = input()
n = 1
lis = []
for i in a:
    if i == "A" or i == "E" or i == "I" or i == "O" or i == "U" or i == "Y":
        n = 1
        lis.append(n)
    else:
        n += 1
        lis.append(n)
print(max(lis))