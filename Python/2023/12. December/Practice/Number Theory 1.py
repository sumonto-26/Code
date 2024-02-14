'''
Given a number N. Print its factorial.
Constraints 
1 <= N<= 100
# print answer modulo M where M = 47


'''

n = int(input())
M = 10**9+7
factorial = 1
for i in range(2, n+1):
    factorial = (factorial * i) % M
print(factorial) # 5:17



