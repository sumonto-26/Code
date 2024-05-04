s = input()
# alphabets = list(set(list(s))) # it shuffle the set
alphabets = [char for index, char in enumerate(s) if char not in s[:index]]
ans = ""
for i in alphabets:
    c = s.count(i)
    if c == 1:
        ans = i
        break
if ans != "":
    print(s.index(ans), ans, alphabets)
else:
    print(-1)