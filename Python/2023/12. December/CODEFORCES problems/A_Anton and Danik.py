a = int(input())
b = input()

Anton = b.count('A')
Danik = b.count('D')

if Anton > Danik:   print("Anton")
if Danik > Anton:   print("Danik") # Right Way ++ 
if Anton == Danik:   print("Friendship")