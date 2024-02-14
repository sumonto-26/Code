# DATE--> 19 December 2023
# 6:51 kamnay hoilo jani na vhabjilam ki 5 no test a error chamu
# dakhi ki Accepted

i = int(input())
a = input()
n = []
o = a.count("n")
z = a.count('z')
if o >=1:
    n.append('1 '*o)
    if z >= 1:
        n.append(' 0'*z)
else:
    n.append(' 0'*z)

print(''.join(n))