# Date ==> 5 April 2024
# MY LOGIC
# ACCEPTED!
a = int(input())
for i in range(1, a+1):
    if ((a-i)-i)%3 != 0 and i%3 != 0:
        print(f"{i} {i} {(a-i)-i}")
        break
