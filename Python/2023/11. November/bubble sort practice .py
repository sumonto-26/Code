def bubble_sort(arr):

    n = len(arr)

    for i in range (n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                a = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = a

    return arr

my_list1 = [10, 5, 3, 8, 2, 9, 1]

a = bubble_sort(my_list1)
print( a )