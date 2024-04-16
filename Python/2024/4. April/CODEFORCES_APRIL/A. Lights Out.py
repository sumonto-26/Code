def swap(x):
    return 1 if x == 0 else 0

# Reading input and splitting into integers
a, b, c = map(int, input().split())
d, e, f = map(int, input().split())
g, h, i = map(int, input().split())

# Creating the array
array = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]

# Checking and swapping
if a % 2 != 0:  
    array[0][:2] = [swap(x) for x in array[0][:2]]
    array[1][0] = swap(array[1][0])
if b % 2 != 0:
    array[0][:] = [swap(x) for x in array[0][:]]
    array[1][1] = swap(array[1][1])
if c % 2 != 0:
    array[0][1:] = [swap(x) for x in array[0][1:]]
    array[1][2] = swap(array[1][2])
if d % 2 != 0:
    array[0][0] = swap(array[0][0])
    array[1][:2] = [swap(x) for x in array[1][:2]]
    array[2][0] = swap(array[2][0])
if e % 2 != 0:
    array[1][:] = [swap(x) for x in array[1][:]]
    array[0][1] = swap(array[0][1])
    array[2][1] = swap(array[2][1])
if f % 2 != 0:
    array[0][2] = swap(array[0][2])
    array[1][1:] = [swap(x) for x in array[1][1:]]
    array[2][2] = swap(array[2][2])
if g % 2 != 0:
    array[2][:2] = [swap(x) for x in array[2][:2]]
    array[1][0] = swap(array[1][0])
if h % 2 != 0:
    array[2][:] = [swap(x) for x in array[2][:]]
    array[1][1] = swap(array[1][1])
if i % 2 != 0:
    array[1][2] = swap(array[1][2])
    array[2][1:] = [swap(x) for x in array[2][1:]]

# Printing the modified array
for row in array:
    print(''.join(map(str, row)))