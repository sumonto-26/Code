# DATE ==> 12 June 2024
# TOPIC ==> - Dictionaries, Nesting and the Secret Auction.

# Dictionaries = {
    # key1: value1,
    # key2: value2,...}
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    123: "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
}

print(programming_dictionary, "\n")

#Retrieving items from dictionary.
"""print(programming_dictionary["Bug"], "\n")
print(programming_dictionary[123], "\n")
print(programming_dictionary["Loop"], "\n")
print(programming_dictionary)"""

# Adding new items or edit any items in dictionary.
programming_dictionary["Loop"] = "The Action Of Doing Something Over And Over Again."
programming_dictionary["Variables"] = "A Container to store some data."

print(programming_dictionary, "\n")

# Create An Empty Dictionary.
empty_dictionary = {} 

# Clear a Dictionary.
'''programming_dictionary = {}
print(programming_dictionary)'''

# Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])