# DATE ==> 3 September 2024
# ATUHOR ==> SUMONTO

'''
Problem B. osu!mania.
You are playing your favorite rhythm game, osu!mania. The layout of your beatmap consists of n rows and 4
columns. Because notes at the bottom are closer, you will process the bottommost row first and the topmost row last.
Each row will contain exactly one note, represented as a '#'.
For each note 1,2,…,n, in the order of processing, output the column in which the note appears.
'''
# SOLUTION
for _ in range(int(input())):
    arr = []
    n = int(input())
    for i in range(n):
        s = input()
        x = s.find("#")
        arr.append(str(x+1))
    print(" ".join(arr[::-1]))
    

'''
Problem C. The Legend of Freya the Frog.
Freya the Frog is traveling on the 2D coordinate plane. She is currently at point (0,0) and wants to go to point (x,y)
In one move, she chooses an integer d such that 0 ≤ d ≤ k and jumps d  spots forward in the direction she is facing.
Initially, she is facing the positive x direction. After every move, she will alternate between facing the positive x 
direction and the positive y direction (i.e., she will face the positive y direction on her second move, the positive x
direction on her third move, and so on).
What is the minimum amount of moves she must perform to land on point (x,y)?
'''
# SOLUTION
for _ in range(int(input())):
    x,y,k = map(int,input().split())
    steps_x = (x + k - 1) // k  # Ceil(x / k)
    steps_y = (y + k - 1) // k  # Ceil(y / k)
    i = max(2 * steps_x - 1, 2 * steps_y)
    print(i)