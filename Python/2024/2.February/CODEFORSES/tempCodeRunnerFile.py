for _ in range(int(input())):
    a = int(input())
    
    total_digit_sum = 0
    
    for i in range(1, a + 1):
        num = i
        while num > 0:
            total_digit_sum += num % 10
            num //= 10
    
    print(total_digit_sum)
