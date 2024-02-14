# 2 December 2023
# nijer thika # In myself it's my logic

n = 0
a = input()
for i in range(int(a)):
    input_string = input()
    my_list = [int(x) for x in input_string.split()]

    if int(my_list[0]) > int(my_list[1]):
        n += 1
print(n)
# 10 ta thika 11:12 pojonto parinai arpor  daika liksi

# _=input
# x,y=zip(*[_().split()for i in'_'*int(_())])
# print(sum(x.count(i)for i in y))
