# DATE --> 4 January 2024
# TIME COMPLEXITY --> 46ms 
# ACCEPTED in 1st try
# RATING --> 800

# my logic
n = []
for i in range(1,1667):
    if i%3 == 0 or str(i)[-1] == '3':   pass
    else:   n.append(i)
    
for _ in range(int(input())):
    b = int(input())
    print(n[b-1])


# anshul_2010's code
'''
t=int(input())
k=[]
for i in range(1667):
    if(i%3!=0 and i%10!=3):
        k.append(i)
for i in range(t):
    n=int(input())
    print(k[n-1])'''