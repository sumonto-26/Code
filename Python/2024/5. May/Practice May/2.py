def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2 
        left_half = arr[:mid] 
        right_half = arr[mid:]

        merge_sort(left_half)  
        merge_sort(right_half) 

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Example usage:
arr = list(map(int,input().split()))
merge_sort(arr)
print("Sorted array:", arr)


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # Current element to be compared
        j = i - 1

        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example usage:
arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print("Sorted array:", arr)

