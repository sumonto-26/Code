a = int(input())
a1 = str(a+1)
n = False

while n == False:
    
    if a1[0] != a1[1] and a1[0] != a1[2] and a1[1] != a1[2] and a1[2] != a1[3] and a1[3] != a1[0] and a1[1] != a1[3] and a1[2] != a1[3] :
        break
    else:
        a1 = int(a1)
        a1 += 1
        a1 = str(a1)

  
print(a1)
