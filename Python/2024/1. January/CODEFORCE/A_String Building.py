# Date --> 8 January 2024
a = input()
a1 = a[0]
a2 = a[1]
if a1 == "a" or a1 == "h" :
    if a2 == '8' or a2 == "1":
        print("3")
    else:    
        print('5')
else:
    if a2 == '8' or a2 == '1':
        print("5")
    else:
        print("8")