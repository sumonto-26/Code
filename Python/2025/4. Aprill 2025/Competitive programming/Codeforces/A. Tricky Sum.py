# AUTHOR ----> SUMONTO
# DATE ------> 5/April/2025
power_of_2 = [2**i for i in range(32)]
for _ in range(int(input())):
    n = int(input())
    correct_index = 0
    while(n>=power_of_2[correct_index]):
        correct_index +=1
    ans = (n*(n+1))//2
    print(ans - (2*(power_of_2[correct_index]-1)))
    