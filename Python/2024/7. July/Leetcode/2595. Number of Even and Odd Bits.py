# DATE ==> 27 JULY 2024
# TIME ==> 7:13 AM
# AUTHOR ==> SUMONTO

n = int(input())
b = bin(n)[::-1]
fir = sec = 0
for i in range(len(b)):
    if b[i] == '1' and i%2 == 0: fir += 1
    elif b[i] == "1" and i%2 == 1: sec += 1
print([fir,sec])