"""def show(n):
    if n == 0:
        return 0
    else:
        show(n-1)
        print(n)
        
show(5)

def product(n, i = 1):
    if i == len(n):
        return 1
    else:
        # product(n, i+1)
        return n[i] * product(n, i+1)
    
n = list(map(int,input().split()))
answer = product(n)
print(answer)


def sum____(n, i=0):
    if i == len(n):
        return 0
    else:
        return n[i] + sum____(n, i+1)
    
n = list(map(int,input().split()))
ans = sum____(n)
print(ans)


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
n = int(input("Enter a Number: "))
ans = factorial(n)
print(f"Factorial of {n} is {ans}.")
"""

def fibonachi_upto_n(n):
    if n <= 1:
        return n
    else:
        return fibonachi_upto_n(n-1) + fibonachi_upto_n(n-2)
n = int(input("Enter a number: ")) 
for i in range(n):
    ans = fibonachi_upto_n(i)
    print(ans, end = " ")