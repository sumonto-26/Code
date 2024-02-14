a = int(input('Type your first number: '))
b = int(input('Type your second number: '))
# user's opperator
c = (input("\nType + , - , x or / "))
if c == "+" :
  print (  a, "+",b,"=", a+b)
elif c == '-' :
  print (  a, '-',b,"=", a-b)
elif c == 'x' :
  print (  a, 'x',b,"=", a*b)
else :
  print (  a, '/',b,"=", a/b)  