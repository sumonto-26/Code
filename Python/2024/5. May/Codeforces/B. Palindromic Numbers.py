# DATE ==> 4 May 2024
# AUTHOR ==> SUMONTO

for _ in range(int(input())):
    n = int(input())
    the_number = int("9"*n)
    the_number_2 = int("1"*(n+1))
    nd = int(input())
    if str(nd)[0] == "9":
        print(the_number_2-nd)
    else:
        print(the_number-nd)
    