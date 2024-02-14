a = int(input())
for i in range(0,a):
    b = int(input())

    if b >= 1900:
        print("Division 1")
    if b >= 1600 and b <= 1899:
        print("Division 2")
    if b >= 1400 and b <= 1599:
        print("Division 3")
    if b <= 1399:
        print("Division 4")