n = list(map(int,input().split(" ")))
a,b,c,d = n[0],n[1],n[2],n[3]

if a < b and c > d :
    print("Vasya")
elif a > b and c < b:
    print("Misha")
else:
    print("Tie")