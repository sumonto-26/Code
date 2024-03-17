# C. Word on the Paper
for _ in range(int(input())):
    l = ""
    for _ in range(8):
        a = input()
        l += a
    ans = l.replace(".", "")
    print(ans)
    