a,b = map(int,input().split(" "))
digit_list = []
while b > 1:
    for i in range(9,-1,-1):
        if b > i:
            b -= i
            digit_list.append(str(i))
            digit_list.append(str(b))
            break
maximum = "".join(reversed(sorted(digit_list)))
print(maximum)