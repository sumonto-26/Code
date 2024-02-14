a = int(input())

for i in range(a):
    b = list(map(int, input()))


    if b[0]+ b[1]+ b[2] == b[3]+ b[4]+ b[5]:
        print("YES")

    else:
        print("NO")