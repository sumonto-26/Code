def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        key_1 = i - 1
        while key_1 >= 0 and key < arr[key_1]:
            arr[key_1 + 1] = arr[key_1]
            key_1 -= 1
        arr[key_1 + 1] = key


# Example usage:
my_list = [12, 11, 8, 10, 1, 13, 5, 6]
insertion_sort(my_list)
print("Sorted array:", my_list)
