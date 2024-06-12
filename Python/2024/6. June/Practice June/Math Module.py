import math

# 1. Floor
# Round Down a Float Number.
n1 = 10.9
print(f"10.9 with floor method ==> {math.floor(n1)}")

# 2. Ceil
# Round Up a Float Number.
n2 = 10.01
print(f"10.01 with ceil method ==> {math.ceil(n2)}")

# 3. Fabs
# Return the Positive value.
n3 = -10000
print(f"-10000 with fabs method ==> {math.fabs(n3)}")

# 4. Factorial
# Return the Factorial of a Number.
n4 = 5
print(f"Factorial of 5 is ==> {math.factorial(n4)}")

# 5. Fsum
# Return the Sum of an Array or Tuple ...
n5 = [4,3,2,5.2,6,4]
print(f"[4,3,2,5.2,6,4] with fsum method ==> {math.fsum(n5)}")

# 6. Sqrt
# Return the Square Root of a Number.
n6 = 16
print(f"16 with sqrt method ==> {math.sqrt(n6)}")

# 7. Gcd
# Return the Gcd of Some Numbers.
x1 = 50
y1 = 25
print(f"Find GCD of 50 and 25 and 10 with gcd method ==> {math.gcd(x1,y1,10)}")

# 8. Lcm
# Return the Lcm of Some Numbers.
x2 = 50
y2 = 25
print(f"Find Lcm of 50 and 25 and 10 with lcm method ==> {math.lcm(x2,y2,10)}")