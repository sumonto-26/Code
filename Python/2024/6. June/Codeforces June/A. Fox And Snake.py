# DATE ==> 8 June 2024
# AUTHOR ==> SUMONTO
odds = [i for i in range(1,50,2)]
a,b = map(int,input().split())
for i in range(a):
    if i % 2 == 0: 
        print("#"*b)
    else:
        if odds.index(i) % 2 == 0:
            print(("."*(b-1)) + "#")
        else:
            print("#" + ("."*(b-1)))