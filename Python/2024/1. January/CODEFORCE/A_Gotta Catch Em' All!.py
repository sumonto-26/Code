# Date ==> 18 January 2023
a = input()
n = []
ans = []
s = "Bulbasr"
for i in s:
    an = a.count(i)
    n.append(an)

c = [1,2,1,1,2,1,1]
for j in range(len(c)):
    n[j] /= c[j]
    ans.append(n[j])
    
print(int(min(ans)))