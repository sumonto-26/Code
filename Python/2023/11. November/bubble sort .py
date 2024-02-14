def bubble_sort(arr):
    
    n = len(arr) #11

    # Traverse through all array elements
    for i in range(n): # 0 - 10

        # Last i elements are already in place, so we don't need to check them
        for j in range(0, n-i-1): # 0 - 11-0-1  = 10
                                  # 0 - 11-1-1  = 9
                                  # 0 - 11-2-1  = 8
                                  # 0 - 11-3-1  = 7
                                  # 0 - 11-4-1  = 6
                                  # 0 - 11-5-1  = 5
                                  # 0 - 11-6-1  = 4
                                  # 0 - 11-7-1  = 3
                                  # 0 - 11-8-1  = 2
                                  # 0 - 11-9-1  = 1
            
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                b = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = b
        #     print(f"{i}")
        # print("\n")







# Example usage:
my_list1 = [10, 7, 2, 9, 4, 8, 1, 3, 5, 0, 6]
my_list2 = [20, 17, 12, 19, 14, 18, 11, 13, 15, 10, 16]
        
bubble_sort(my_list1)
bubble_sort(my_list2)

print(f"\nSorted list 1: {my_list1} " )
print(f"Sorted list 2: {my_list2} \n" )
