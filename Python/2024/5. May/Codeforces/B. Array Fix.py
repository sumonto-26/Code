# DATE ==> 4 May 2024
# AUTHOR ==> SUMONTO

def sum_digit(i):
    digit_sum = 0
    while i:    
        digit_sum += i % 10
        i //= 10
    return digit_sum

l = [0]
for i in range(1, 200002):
    sum_ = sum_digit(i)+l[i-1]
    l.append(sum_)
    
for _ in range(int(input())):
    a = int(input())
    print(l[a])