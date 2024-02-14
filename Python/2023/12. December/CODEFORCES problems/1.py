a = int(input())
for i in range(a):

    b = int(input())
    c = list(map(int, input().split(" ")))
    mini = min(c)
    new = [mini+1 if x == mini else x for x in c]

    


    print(ans)