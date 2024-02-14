# import time
# print('a')
# time.sleep(1)
# print('b')
# time.sleep(1)
# print('c')
# time.sleep(1)
# print('d')
# time.sleep(1)
# print('e')
# time.sleep(1)
# print('f')
# time.sleep(1)
# print('g')
# time.sleep(1)
# print('h')
# time.sleep(1)
# print('i')
# .....................................



# COPY BY CHATGPT

# SHORTCURT
# import time

# for letter in 'abcdefghijklmnopqrstuvwxyz':
#     print(letter)
#     time.sleep(0.3)





# import time

# fruit = ['mango', 'banana','coconut', 'nut', 'apple', 'watermelon']
# for letter in fruit:
#     print(letter)
#     time.sleep(1)




import time

# Get user input for the sleep duration
try:
    letter = str(input("Enter your name: "))
    sleep_duration = float(input("Enter the number of seconds to sleep between each letter: "))
except ValueError:
    print("Invalid input. Using default sleep duration of 1 second.")
    sleep_duration = 1

# Print letters with user-specified sleep duration
for letter in letter:
    print(letter)
    time.sleep(sleep_duration)

print("Done!")



# MAKE A CLOCK
# import time

# while True:
#     # Get the current time
#     current_time = time.strftime("The time is %H:%M:%S", time.localtime())

#     # Print the current time
#     print(current_time, end="\r")  # Use carriage return to overwrite the previous time
#     time.sleep(0.1)  # Update the time every second

