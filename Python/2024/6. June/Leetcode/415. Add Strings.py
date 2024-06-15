# DATE ==> 13 JUNE 2024
# BEST CODE.


num1 = input()
num2 = input()
i = len(num1)-1
j = len(num2)-1
total = []
carry = 0
while j>=0 or i>=0:
    temp = 0
    if j >= 0:
        temp += (ord(num2[j]) - ord('0'))
        j-=1
    
    if i >= 0:
        temp += (ord(num1[i]) - ord('0'))
        i-=1
    
    temp += carry
    if temp <= 9:
        total.append(temp)
        carry = 0
    else:
        total.append(temp%10)
        carry = temp//10
    
if carry:
    total.append(carry)
returnstr = ""
for i in range(len(total) - 1, -1, -1):
    returnstr = returnstr + str(total[i])
