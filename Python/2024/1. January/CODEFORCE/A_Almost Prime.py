# Date 28 January 2024
def prime_divisors(num):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    divisors_list = []
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            divisors_list.append(i)
            if num // i != i:
                divisors_list.append(num // i)

    prime_divisors_list = [divisor for divisor in divisors_list if is_prime(divisor)]

    return prime_divisors_list

n = 0
a = int(input())
for i in range(1,a+1):
    d = prime_divisors(i)
    if len(d) == 2:
        n += 1
print(n)