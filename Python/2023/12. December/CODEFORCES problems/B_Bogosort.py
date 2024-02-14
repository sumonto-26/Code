import random
for _ in range(int(input())):
    i = int(input())
    a = list(map(str,input().split(" ")))
    random.shuffle(a)
    ans = ' '.join(a)
    print(ans)