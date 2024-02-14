a = input()
keys = "qwertyuiopasdfghjkl;zxcvbnm,./"
b = input()
n = ""
if a == "L":
    for i in b:
        if i in keys :
            ele = keys.index(i)+1
            n = n + keys[ele]

if a == "R":
    for i in b:
        if i in keys :
            ele = keys.index(i)-1
            n = n + keys[ele]


print(n)