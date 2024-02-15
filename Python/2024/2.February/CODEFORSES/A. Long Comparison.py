# DATE ==> 9 February
for _ in range(int(input())):
    a = list(map(int, input().split(" ")))
    b = list(map(int, input().split(" ")))
    
    if (a[0] * (10**a[1]))  > (b[0] * (10**b[1])):
        print(">")
    elif (a[0] * (10**a[1]))  < (b[0] * (10**b[1])):
        print("<")
    else: 
        print("=")
