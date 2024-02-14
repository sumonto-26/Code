# DATE ==> 9 January 2023
# my logic
a = input()
if '5 of week' in a or '6 of week' in a: print("53")
elif 'of week' in a : print("52")
elif '30 of month' in a : print("11")
elif '31 of month' in a :  print("7")
else: print("12")