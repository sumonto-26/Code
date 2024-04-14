for _ in range(int(input())):
    n = int(input())
    a = input()
    pos = [0, 0]
    ans = "NO"
    for i in a:
        if i == "U": pos[1] += 1
        if i == "D": pos[1] -= 1
        if i == "R": pos[0] += 1
        if i == "L": pos[0] -= 1
        if pos[0] == 1 and pos[1] == 1:
            ans = "YES"
            break
    print(ans)