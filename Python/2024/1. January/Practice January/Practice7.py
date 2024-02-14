'''# O(n)
def prime_factorization():
    prime_factors = []
    num = int(input("Enter a number:  "))
    
    for i in range(2,num):
        while num % i == 0 :
            prime_factors.append(str(i))
            num //= i

    for prime in prime_factors:
        print (prime, end = " ")

prime_factorization()

'''


# Time Complexity == O(sqrt(num))
def prime_factorization():
    prime_factors = []
    num = int(input("Enter a number:  "))

    for i in range(2, int(num ** 0.5)+1):
        while num % i == 0 :
            prime_factors.append(str(i))
            num //= i

    if num > 1:
        prime_factors.append(str(num))

    for prime in prime_factors:
        print (prime, end= " ")


pf = prime_factorization()