# Date --> 3 January 2023

n = set()
a = input()
b = input()
c = input()
win = "F"
s = {a, b, c}
n.update(s)

if (a == 'paper' and (b == 'rock' and c == 'rock')) or (a == 'rock' and (b == 'scissors' and c == 'scissors')) or (a == 'scissors' and (b == 'paper' and c == 'paper')):
    print('F')
elif (b == 'paper' and (a == 'rock' and c == 'rock')) or (b == 'rock' and (a == 'scissors' and c == 'scissors')) or (b == 'scissors' and (a == 'paper' and c == 'paper')):
    print('M')
elif (c == 'paper' and (a == 'rock' and b == 'rock')) or (c == 'rock' and (a == 'scissors' and b == 'scissors')) or (c == 'scissors' and (a == 'paper' and b == 'paper')):
    print('S')
else:
    print("?")
    