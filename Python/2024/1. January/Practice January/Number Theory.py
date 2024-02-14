# DATE ---> 26 January 2024 
# FRIDAY

import math

class NumberTheory:
    @staticmethod
    def gcd(a, b):
        if a == 0:
            return b
        if b == 0:
            return a
        if b > a:
            return NumberTheory.gcd(b % a, a)
        return NumberTheory.gcd(a % b, b)

    @staticmethod
    def lcm(a, b):
        return (a * b) // NumberTheory.gcd(a, b)

    @staticmethod
    def gcd_of_list(numbers):
        # Calculate GCD of a list of numbers
        result = numbers[0]
        for num in numbers[1:]:
            result = math.gcd(result, num)
        return result

    @staticmethod
    def lcm_of_list(numbers):
        # Calculate LCM of a list of numbers
        result = numbers[0]
        for num in numbers[1:]:
            result = result * num // math.gcd(result, num)
        return result

    @staticmethod
    def divisor(num):
        s = int(math.sqrt(num))
        n = []
        for i in range(1, s + 1):
            if num % i == 0:
                n.append(i)
                if num // i != i:
                    n.append(num // i)
        return sorted(n)

    @staticmethod
    def all_divisors_up_to_n(n):
        divisors = [[] for _ in range(n + 1)]
        for d in range(1, n + 1):
            for a in range(d, n + 1, d):
                divisors[a].append(d)
        return divisors

    @staticmethod
    def sieve_of_eratosthenes(n): # all primes between 2 - n
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        primes = []
        for current_number in range(2, n + 1):
            if is_prime[current_number]:
                primes.append(current_number)
                for multiple in range(current_number * current_number, n + 1, current_number):
                    is_prime[multiple] = False
        return primes

    @staticmethod
    def prime_factorization(n):
        if n <= 1:
            return "Prime factorization is not defined for numbers less than or equal to 1."

        factors = []
        i = 2
        while i * i <= n:
            if n % i == 0:
                power = 0
                while n % i == 0:
                    power += 1
                    n //= i
                factors.append((i, power))
            i += 1

        if n != 1:
            factors.append((n, 1))

        formatted_factors = []
        for factor, power in factors:
            if power > 1:
                formatted_factors.append(f"{factor}^{power}")
            else:
                formatted_factors.append(str(factor))

        result = " x ".join(formatted_factors)
        return result

    @staticmethod
    def is_prime(num):
        if num <= 1:
            return "not prime"
        else:
            for i in range(2, int(math.sqrt(num))+1):
                if num % i == 0:
                    return "not prime"
        return "prime"
                
                
                
number_theory = NumberTheory()

# Prime check
number = int(input("Enter a number to check if it is prime: "))
check_prime = number_theory.is_prime(number)
print(f"{number} is {check_prime}\n")

# 2 number GCD calculation
a_gcd = int(input("Enter the first number for GCD: "))
b_gcd = int(input("Enter the second number for GCD: "))
gcd_result = number_theory.gcd(a_gcd, b_gcd)
print(f"GCD: {gcd_result}\n")

# 2 number LCM calculation
a_lcm = int(input("Enter the first number for LCM: "))
b_lcm = int(input("Enter the second number for LCM: "))
lcm_result = number_theory.lcm(a_lcm, b_lcm)
print(f"LCM: {lcm_result}\n")

# list gcm claculation
a_multiple_gcd = list(map(int,input("Make list of number for calculating gcd : ").split(" ")))
multiple_gcd_result = number_theory.gcd_of_list(a_multiple_gcd)
print(f"GCD of {a_multiple_gcd} is {multiple_gcd_result}\n")

# list lcm claculation
a_multiple_lcm = list(map(int,input("Make list of number for calculating lcm : ").split(" ")))
multiple_lcm_result = number_theory.lcm_of_list(a_multiple_lcm)
print(f"LCM of {a_multiple_lcm} is {multiple_lcm_result}\n")


# Divisor calculation
num = int(input("Enter a number for divisor calculation: "))
divisor_result = number_theory.divisor(num)
print(f"Divisors of {num} are {divisor_result}\n")

# All divisors up to n
n_for_divisors = int(input("Enter a value for calculating all divisors up to n: "))
all_divisors_result = number_theory.all_divisors_up_to_n(n_for_divisors)
print(f"All Divisors between 0-{n_for_divisors} are {all_divisors_result}\n")

# Primes up to n using Sieve of Eratosthenes
n_for_sieve = int(input("Enter a value for printing primes between 1 to n: "))
prime_2_n = number_theory.sieve_of_eratosthenes(n_for_sieve)
print(f"All prime numbers between 1-{n_for_sieve} are {prime_2_n}\n")

# Prime factorization
num_for_prime_factorization = int(input("Enter a number for prime factorization: "))
prime_factorization_result = number_theory.prime_factorization(num_for_prime_factorization)
print(f"{num_for_prime_factorization} = {prime_factorization_result}")