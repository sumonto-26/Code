def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1], arr[j] = arr[j], arr[j + 1] # Swaping
            j -= 1

# Example usage:
my_array = list(map(int,input("Type Your Array: ").split()))
insertion_sort(my_array)
print("Sorted array:", my_array)
