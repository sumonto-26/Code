# Date ==> 28 January 2023
def prime_divisor(number):
    
    def prime(num):
        if num >= 2:
            for i in range(2,int(num**0.5)+1):
                if num % i == 0 :
                    return False
            return True
        
    n = []
    for i in range(1,int(number ** 0.5)+1):
        if number % i == 0:
            n.append(i)
            if number//i != i:
                n.append(number//i)

    ans = [i for i in n if prime(i)]

    return ans

for _ in range(int(input())):
    a = list(map(int,input().split(" ")))
    dif = a[0]-a[1]
    ans = 0
    pd = prime_divisor(dif)
    for i in pd:
        if dif % i == 0:
            ans += 1
    if ans != 0:
        print("YES")
    else:
        print("NO", pd)
    
    
# Correct way but Time error
# Correct way but Time error
# Correct way but Time error
# Correct way but Time error
# Correct way but Time error
# Correct way but Time error
# Correct way but Time error
# Correct way but Time error
# Correct way but Time error
# Correct way but Time error
# Correct way but Time error