print ("WELCOME TO SUMONTO'S TABLE MAKER\n")
# DATE-9-MAY-2023

try:
    a = int (input('Type number to make table:\n= '))
    for i in range( 1,11): 
        b = (i * a)
        print (f"{a} x {i} = {b}" )
except:
    print("\nType only number not anything else")
else:
    print("\nThanks for use this 'Table Maker' ")
