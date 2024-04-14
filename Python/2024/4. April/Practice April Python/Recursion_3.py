a = int(input())
def fibbonachi(a):
    if a < 2:
        return a
    if a == 2:
        return 1
    else:
        return (fibbonachi(a-1) + fibbonachi(a-2))

print(f"Fibonacci series of {a} numbers is :", end = " ")
for i in range(0,a):
    ans = fibbonachi(i)
    print(ans, end = " ")