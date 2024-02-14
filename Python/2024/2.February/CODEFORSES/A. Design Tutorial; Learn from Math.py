# Date ==> 8 February 2024
# my logic

def find_composite(num):
    if num <= 1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return True
        
a = int(input())
for i in range(a):
    if find_composite(i):
        if find_composite(a-i) == True:
            print(i, a-i)
            break