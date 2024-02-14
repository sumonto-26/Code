a = int(input())
n = []
for i in range(a*3):
    b = input()
    if '?'in b :
        if "B" in b and 'C' in b :
            n.append("A")
        elif 'A' in b and 'B' in b:
            n.append('C')
        else:
            n.append("B")
ans = ' \n'.join(n)
print(ans)