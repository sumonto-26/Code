# DATE ==> 17 February 2025
# YOUTUBE VIDEO LINK =====> https://www.youtube.com/watch?v=HeW-D6KpDwY&t=180s&ab_channel=ShradhaKhapra

"""
# Creating class
class Student:
    name = "J kono Name"
    print (name)
    
    school_name = "SPSC" # Class Attributes
    college_name = "NDC"
   
    # Constructor.
    def __init__(self): # 1. DEFAULT CONSTRUCTORS
        print("Default Constructor.")
        
    # 2. Parameterized constructors
    def __init__(self, name, roll):
        print (self)
        self.name = name  # Object Attributes > Class Attr..
        self.roll = roll+1
        self.roll_num = roll+2
        
        print(self.name)
        print("Adding new student in database...")
        print(f"Name ===> {name} \nRoll number ===> {self.roll_num}")
        print(roll, self.roll, self.roll_num)
        
    def welcome(self): # Method
        print("Welcome Student")
    
    def get_marks(self): # Method
        return self.roll*20

# Creating object (instance || or || instance of class)

print(Student.college_name)
print(Student("Tamim", 1).school_name)

s1 = Student("Sumonto", 6)
print(s1.name, s1.roll)
print(s1.college_name)
print(s1)
print(s1.name)
s1.welcome()
print(s1.get_marks())

s2 = Student("Sadat", 3)
print(s2.name, s2.roll)
print(s2.school_name)


# Another class
class Car:
    color = "Blue"
    brand = "BMW"
    
car1 = Car()
print(car1.color)
print(car1.brand)

car2 = Car()

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
            
    def get_avg(self):
        sum = 0
        num = 0
        for val in self.marks:
            sum += val 
            num += 1
        print("Hi", self.name, "your avg score is :", sum/num)

s1 = Student("Tony Stark", [99,98,97])
s1.get_avg()

s1.name = "Iron Man"
s1.marks = [55, 99, 80]
s1.get_avg()

class Car:
    car_price = 1000000
    def __init__(self):
        print(f"Car Price is {self.car_price}")
        
    @staticmethod
    def car_petrol(car_price):
        car_ptrol = car_price/500
        print(car_ptrol, "-----")
        return car_ptrol
        
car1 = Car()
Car.car_petrol(5000)
car1.car_petrol(5000)
print(car1.car_petrol(5000))
"""


# What is Abstraction? 
# Hiding the implementation details of a class and only showing the essential features to the user.
class Account:
    def __init__ (self, bal, acc):
        self.balance = bal
        self.account_num = acc
    
    def debit(self, amount):
        self.balance -= amount  
        print("Rs.", amount, "was debited")
        print("total balance = ", self.get_balance())
    
    def credit(self, amount):
        self.balance += amount  
        print("Rs.", amount, "was credited")
        print("total balance = ", self.get_balance())
    
    def get_balance(self):
        return self.balance
    
acc1 = Account(10000, 12345)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(5000)
acc1.debit(1000)
# print(acc1.balance)
# print(acc1.account_num)

# What is Encapsulation?
# Wrapping data and functions into a single unit(object)