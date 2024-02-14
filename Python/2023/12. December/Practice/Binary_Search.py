def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        # mid = (low + high) // 2
        mid = low + (high - low) // 2
        mid_val = arr[mid]

        if mid_val == target:
            return mid  # Element found, return its index
        elif mid_val < target:
            low = mid + 1  # Search in the right half
        else:
            high = mid - 1  # Search in the left half

    return -1  # Element not found

# Example usage:
sorted_array = [i for i in range(1,101)]
target_element = int(input())
result = binary_search(sorted_array, target_element)

if result != -1:
    print(f"Element {target_element} found at index {result}.")
else:
    print(f"Element {target_element} not found in the array.")
