# Date ==> 26 February 2024
# My logic
# time complexity ==> 31ms

for _ in range(int(input())):
    a = list(map(int, input().split(" ")))
    b = list(map(int, input().split(" ")))

    d = (max(a) - min(a))* b[0]
    an = min(a)*b[1]
    ans1 = an+d

    print(min(ans1, b[0]*sum(a)))
    
    
# other's logic
# time complexity ==> 30ms
'''
t = int(input())
 
for i in range(t):
    x, y = map(int, input().split())
    a, b = map(int, input().split())
 
    if 2 * a < b:
        print((x + y) * a)
    else:
        print(min(x, y) * b + abs(x - y) * a)'''