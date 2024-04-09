# DATE ==> 9 APRIL 2024
# TIME ==> 1:00 PM
# AUTHOR ==> SUMONTO

l = []
a = int(input())
for i in range(19, 10800101, 9):
    if sum(int(digit) for digit in str(i)) == 10:
        l.append(i)
        if len(l) == a:
            break

print(l[a-1])