def show(n):
    if n == 0:
        return
    print(n)
    show(n-1)
show(5)


"""a = list(map(int,input().split()))
def my_function(a, i=0):
    if i == len(a): 
        return 1
    else:
        return a[i] * my_function(a, i + 1) 
ans1 = my_function(a)
print(f"Product == {ans1}")


def my_sum_function(a, i=0):
    if i == len(a)-1: 
        return a[i]
    else:
        return a[i] + my_sum_function(a, i + 1) 
ans2 = my_sum_function(a)
print(f"Sum == {ans2}")"""


'''
# Dictionary to store computed Fibonacci numbers
fib_cache = {}

def fibonacci(a):
    if a in fib_cache:
        return fib_cache[a]
    if a <= 1:
        return a
    else:
        fib_cache[a] = fibonacci(a-1) + fibonacci(a-2)
        return fib_cache[a]

a = int(input("Enter a number: "))
for i in range(0, a+1):
    ans = fibonacci(i)
    print(ans, end = "\n\n")
'''

"""n = int(input())
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(n)) 
"""


