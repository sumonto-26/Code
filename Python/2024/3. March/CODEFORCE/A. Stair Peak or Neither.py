for _ in range (int(input())):
    a = list(map(int,input().split(" ")))
    if a[0] < a[1] and a[1] < a[2]:
        print ("STAIR")
    elif a[0] < a[1] and a[1] > a[2]:
        print ("PEAK")
    else:
        print("NONE")