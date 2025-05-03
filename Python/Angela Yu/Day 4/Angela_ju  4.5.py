import random
#  Don't change the code below
test_seed = int(input("Creat a seed number: "))
random.seed(test_seed)

# Split string method
namesAsCSV = input("Give me eveybosy's name [Seperated by a comma.] ")
names = (namesAsCSV.split(","))
# Don't change the code above

# Write your code below this line

# Get the total number of items in list.
num_items = len(names) 
# Generate random numbers between 0 and last index of the list
random_choice = random.randint(0, num_items - 1)
person_who_will_pay = names[random_choice]

# person_who_will_pay = random.choice(names) # shot cut
print (person_who_will_pay + " is going to buy the milk today. ")