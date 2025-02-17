# DATE ==> 17 February 2025
# YOUTUBE VIDEO LINK =====> https://www.youtube.com/watch?v=HeW-D6KpDwY&t=180s&ab_channel=ShradhaKhapra
# Finish =====> 38:50 sec 

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
"""

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
