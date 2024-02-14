a = int(input())
lis = ''
h,l,t = "I hate ", "I love ","that "

for i in range(1,a+1):

    if i % 2 == 0:
        if i != a:  lis += l + t
        else:   lis += l + 'it'

    else:
        if i != a:  lis += h + t
        else:   lis += l + 'it'

print(lis)


