# DATE --> 4 January 2024
# TIME -->  10:00am - 10:14am
# TIME COMPLEXITY --> 46ms 
# ACCEPTED in 1st try
# RATING --> 800

# my logic
n = ''
for i in range(334):
    n += 'Yes'
for _ in range(int(input())):
    a = input()
    print("YES" if a in n else "NO")

'''
# m.olimovvv's code
# TIME COMPLEXITY --> 31ms 
# for _ in range(int(input(""))):
#     b = input("")
#     if b in "Yes"*20:
#         print("YES")
#     else:
#         print("NO")'''



