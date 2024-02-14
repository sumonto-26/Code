# (Code With Harry Day-21) date-28-may 2023
# There are 4 type of  Function Argument 
# 1. Default Arguments
# 2. Keyword Arguments
# 3. Variable legth Arguments
# 4. Required Arguments

# DEFAULT ARGUMENTS
def default_average(a=9, b=1):
    print("'default' The average is ", (a+b)/2)
default_average(1,5)
# or default_average(b=9)

# KEYWORD ARGUMENTS
def keyword_average(a=9, b=1):
    print("'keyword' The average is ", (a+b)/2)
keyword_average(b=1, a=5)
 
# VARIABLE LEGTH ARGUMENTS
def variable_legth_average(*numbers):
    print (type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i 
    print("'Variable Legth' Average is: ", sum / len(numbers))
variable_legth_average(5,6,7,8,9,10)    

# REQUIRED ARGUMENTS
def required_average(a=5 , b=1):
    print("'required' The average is ", (a+b)/2)
required_average(a=9, b=10)
# In 'Required Arguments we cannot skip a's value.