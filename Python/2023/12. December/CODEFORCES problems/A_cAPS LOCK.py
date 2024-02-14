# DATE --> 18 December 2023
# My logic 

a = input()
if a[0].islower() and a[1:].isupper() : print(a.title())
elif len(a) == 1 and a.islower():   print(a.upper())
elif len(a) == 1 and a.isupper():   print(a.lower())
elif a.isupper():   print(a.lower())
else:   print(a)

# Other's logic

# s = input().strip()
# if s[0].islower() and (not s[1:] or s[1:].isupper()):
# 	print(s.capitalize())
# elif s.isupper():
#     print(s.lower())
# else:
# 	print(s)