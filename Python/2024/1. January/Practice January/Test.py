import random


def divisor(num):
    divisor_list = []
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            divisor_list.append(i)
            if num // i != i:
                divisor_list.append(num//i)
                
    return sorted(divisor_list)

def gcd1(a,b):
    while b != 0:
        a, b = b, a%b
    return a    
    
def gcd2(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a > b:
        return gcd2(a % b, b)
    
    return gcd2(b % a, a)

def lcm(a, b):
    return a*b // gcd2(a,b)

def is_prime(num):
    if num < 2:
        return "No number is not prime"
    else:
        for i in range(2 , int(num**0.5) + 1):
            if num % i == 0:
                return "No number is not prime"
    return "Yes number is prime"

def sieve_of_eratosthenes(num):
    prime_list = [True] * (num+1)
    prime_list[0] = prime_list[1] = False
    
    for i in range(2, int(num**0.5)+1):
        if prime_list[i] == True:
            for j in range(i*i, num+1, i):
                prime_list[j] = False
    return [ans for ans in range(2, num+1) if prime_list[ans] == True]
