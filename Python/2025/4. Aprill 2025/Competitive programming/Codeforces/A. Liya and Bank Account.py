n = int(input())
if(n > -11 and n<0): print(0)
elif (n >= 0): print(n)
else:
    last_digit = int(str(n)[-1])
    before_last = int(str(n)[-2])
    if(last_digit >= before_last): print(str(n)[:-1])
    else:
        print(int(str(n)[:-2] + str(n)[-1]))