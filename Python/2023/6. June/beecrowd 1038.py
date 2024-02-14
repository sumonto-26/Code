a = int(input())
if a == 1:
    x = 4
    
elif a == 2:
    x = 4.50
    
elif a == 3:
    x = 5
    
elif a == 4 :
    x = 2
    
elif a == 5 :
    x = 1.50
    
b = int(input())
c = float(x*b) 
d = ("%.2f" % c)

print(f"Total: R$ {d}")