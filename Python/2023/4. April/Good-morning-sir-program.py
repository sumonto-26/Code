import time
t = time.strftime('%H:%M:%S') 
hour = int(time.strftime('%H'))
min = int(time.strftime('%M'))
sec = int(time.strftime('%S'))
#  hour = int(input("Enter hour: "))
print(t)
#  print (min)
#  print (sec)
if(hour>=0 and hour<12):
   print("Good Morning Sir!")
elif(hour>=12 and hour<17):
   print("Good Afternoon Sir!")
else:
   print("Good Night Sir!")