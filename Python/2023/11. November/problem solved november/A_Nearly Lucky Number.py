a = input()
ld= 0

for i in range(len(a)):
    if a[i] == "4" or a[i] =="7":
        ld += 1

if ld == 4 or ld == 7:
    print ("YES")

else:
    print("NO")
