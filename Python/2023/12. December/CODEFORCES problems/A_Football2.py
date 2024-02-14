team1,team2 = 0,0


for i in range(int(input())):
    user = input()
    if i == 0 :
        ti = user
        team1+=1

    if i > 0 and user != ti:
        t2 = user
        team2+= 1
    if i>0 and user == ti:  team1+= 1


print(ti if team1 > team2 else t2)
