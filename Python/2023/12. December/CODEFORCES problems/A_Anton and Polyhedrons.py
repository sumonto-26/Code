# Date --> 14 December 2023 
# //////my logic/////
# submit at 7:01 PM accepted in first try

l = []
a = int(input())

for i in range(a):
    b = input()

    if b == "Tetrahedron":
        l.append(4)

    if b == "Cube":
        l.append(6)

    if b == "Octahedron":
        l.append(8)

    if b == "Dodecahedron":
        l.append(12)

    if b == "Icosahedron":
        l.append(20)

print(sum(l))
