# for _ in range(int(input())):
#     n = []
#     a = list(map(str,input()))
#     for i in range(len(a)):
#         z = a.index(a[i])+1
#         k = len(a)-z
#         ans = str(a[i]) + "0"*k
#         if a[i] != '0':
#             n.append(ans)
#     answer = " ".join(n)
#     print(len(n))
#     print(answer)


for _ in range(int(input())):
    n = []
    a = input().strip()
    for i, digit in enumerate(a):
        if digit != '0':
            ans = digit + "0" * (len(a) - i - 1)
            n.append(ans)
    answer = " ".join(n)
    print(len(n))
    print(answer)

# another code
'''for _ in range(int(input())):
    a = input().strip()
    n = [digit + "0" * (len(a) - i - 1) for i, digit in enumerate(a) if digit != '0']
    answer = " ".join(n)
    print(len(n))
    print(answer)
'''