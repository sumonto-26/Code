n = []

for _ in range(int(input())):
    a = set(map(str, input()))
    if len(a) != 2:
        n.append('bug')

if len(n) == 0:
    if all(n[i - 1] == n[-i] for i in range(1, len(n) // 2 + 1)):
        print("YES")
    else:
        print("NO")
else:
    print("NO")


# NOT COMPELITE!!!!!!!!!!!!!!!!!
# NOT COMPELITE!!!!!!!!!!!!!!!!!
# NOT COMPELITE!!!!!!!!!!!!!!!!!
# NOT COMPELITE!!!!!!!!!!!!!!!!!
# NOT COMPELITE!!!!!!!!!!!!!!!!!
# NOT COMPELITE!!!!!!!!!!!!!!!!!
# NOT COMPELITE!!!!!!!!!!!!!!!!!
# NOT COMPELITE!!!!!!!!!!!!!!!!!
# NOT COMPELITE!!!!!!!!!!!!!!!!!
# NOT COMPELITE!!!!!!!!!!!!!!!!!
# NOT COMPELITE!!!!!!!!!!!!!!!!!