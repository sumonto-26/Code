
'''a, b = map(int, input().split())
for i in range(a):
    for j in range(b):
        print("*", end="")
    print()
'''
# a, b = map(int, input().split())
# for i in range(a):
#     for j in range(b):
#         if i == 0 or i == a-1 or j == 0 or j == b-1 :
#             print ('', end= '')
#         else:
#             print(' ', end='')
#     print()

'''
a = int(input())

for i in range(a, 0, -1):
    for j in range(i):
        print("🟩", end= '')
    print()'''


# a = int(input())
# for i in range(1, a+1):
#     for j in range(1, a+1):
#         if (j <= a-i ):
#             print(" ", end ='')
#         else:
#             print('*', end = '')
#     print()

'''a = int(input())
for i in range(1,a+1):
    for j in range(1, i+1):
        print(i, end= ' ')
    print()'''


# a = int(input())
# c = 1
# for i in range(1,a+1):
#     for j in range(1, i+1):
#         print(c, end= ' ')
#         c+=1
#     print()

a = int(input())
c = 0
for i in range(1,a+1):
    for j in range(1, i+1):
        c+=1
        print(c, end= ' ')
    print()

