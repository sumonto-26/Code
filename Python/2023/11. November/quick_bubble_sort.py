def bubble_sort(arr):
    lens = len(arr)

    for i in range (lens):
        for j in range(0, lens-i-1):

            if arr[j] > arr[j+1]:
                new_var = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = new_var

    return arr


def quick_sort(arr):
    pass








a_list = [9,8,3,6,7,8,1,0,5]
Sorted = bubble_sort(a_list)
print(f"Sorted = {Sorted}")