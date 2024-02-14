# if \ elif \ else

# if condition1:
#     do A
# elif condition2:
#     do B
# else:
#     do C
 
''' MULTIPLE IF
if condition1:
    do A
if condition2:
    do B
if condition3:
    do C '''
    
print ("Welcome to the rollaercoaster!")
height = int(input("Enter your height in cm "))

if height >=120 :
    print ("you can ride the rolarcoster")
    age = int(input("What is your age "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18 :
        bill = 7
        print("Youth tickets are $7.")
    else :
        bill = 12
        print('Adult tickets are $12.')
        
    wants_photo = input("Do you want a photo taken? Y or N.")
    if wants_photo == "Y":
        bill += 3
    
    print(f"Your final bill id {bill}")    

else :
    print("Sorry, you have to grow taller before you can ride.")     