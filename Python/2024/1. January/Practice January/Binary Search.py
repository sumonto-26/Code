# DATE ==> 22 JANUARY 2024

# LENEAR SEARCH CODE

'''def lenear_search(arr,len,x):
    for i in range(len):
        if arr[i] == x:
            return i


arr = [7,8,5,2,3,4,1,10,92,57]
len = len(arr)
print(arr)
x = int(input("lenear search "))

s = lenear_search(arr, len, x)
print(s)
'''

def binary_search(a,n,x):
    s = 0
    e = n - 1
    while e >= s:
        m = (s+e) // 2
        if a[m] == x:
            return m # find x return index
        elif a[m] > x:
            e = m - 1
        else:
            s = m + 1
    return "not in array"

array = [1, 3, 5, 9, 13, 19, 25, 30, 32, 40]
print(array)
lenght = len(array)
target = int(input("BINARY SEARCH:  "))

ans = binary_search(array, lenght, target)
print(f"index {ans}")