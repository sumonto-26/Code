# 2 December 2023
# nijer thika # In myself it's my logic

a = input()
for i in range(int(a)):
    input_string = input()
    my_list = [int(x) for x in input_string.split()]
    if my_list[0] + my_list[1] == my_list[2]:
        print("+")
    if my_list[0] - my_list[1] == my_list[2]:
        print("-")


# other's people code
# for i in range(int(input())):
#     a,b,c = map(int,input(). split())
#     print("+"if a + b == c else "-")

    