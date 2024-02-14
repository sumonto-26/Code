# code with harry day 11 to day 20
#day 11 note 90 - 105
name = "Harry"
friend = "Rohan"
anotherFriend ='Lovish'
apple = ''' He said, 
Hi Harry  
hey I am good 
"I want to eat an apple'''

print("Hello," + name)
# print(apple)
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
# print (naem [5]) #Throws an error
print("Lets use a for loop\n")
for i in name:
    print(i)
#day 12 code with harry 
# note 106 to 118

fruit = "Mango"
mangoLen = len(fruit)
print(mangoLen)
# print(fruit[0:4]) # including 0 but not 4 
# print(fruit[1:4]) # including 1 but not 4 
# print(fruit[ :5])
# print(fruit[0:-3])
# print(fruit[;len(fruit)-3])
print(fruit[-1:len(fruit) - 3])
print(fruit[-3:-1])

# Quick Quiz: 
nm = "Harry"
print(nm[-4:-2])

print ("day 13 code with harry ")
# note 119 to 146 

# String are immutable 
a = "!!!Harry!!!Harry!!!!!!"
print(len(a))
print(a)
print (a.upper())
print (a.lower())
print (a.rstrip("!"))
print (a.replace("Harry", "Sumonto"))
print (a.split(" ")) 
blogHeading = "introduction tO Js"
print (blogHeading.capitalze())

'''str1 = "Welcome to the Console!!!"
print(len(str1.center(50)))'''
print(a. count ("Harry"))

str1 = "Welcome to the Console !!!"
print (str1.endwith("!!!"))