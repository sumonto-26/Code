def solve(x):
    if x == 45: return 123456789
    digits = [9,8,7,6,5,4,3,2,1,0]
    ans = [0]
    while(1):
        sum_ = sum(ans)
        if(x-sum_>= digits[0]):
            ans.append(digits[0])
            digits = digits[1:]
        elif(x-sum_<10 and x-sum_ in digits):
            ans.append(x-sum_)
            digits.remove(x-sum_)
            break
                   
    ans = sorted(ans)
    ans = [str(i) for i in ans]
    return int(''.join(ans))
           
for _ in range(int(input())):
    x = int(input())
    if(x<10): print(x)
    elif(x>45): print('-1')
    else:
        print(solve(x))