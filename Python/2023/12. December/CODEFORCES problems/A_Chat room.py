# date 3 december 2023
s = input()
com = "hello"
index = 0

for i in range (len(s)):
    if com[index]==s[i] :
        index += 1
    if index == 5:
        break

print("YES" if index == 5 else "NO")