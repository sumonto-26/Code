# QUICK SORT
# Approach 2: Quicksort using list comprehension

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)

def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j>=0 and key<arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

def binary_search(arr, target):
    start = 0
    end = len(arr)-1
    while(start <= end):
        mid = (start+end)//2
        if arr[mid] < target:
            start = mid+1
        elif arr[mid] > target:
            end = mid-1
        else:
            return f"Target in {mid}th index."
    return "Not found!"

def merge_sort(arr):
    if len(arr) > 1:
        # DIVIDE
        mid = len(arr)//2
        left_side = arr[:mid]
        right_side = arr[mid:]
        merge_sort(left_side)
        merge_sort(right_side)
        
        # MERGE
        i = j = k = 0
        while i < len(left_side) and j < len(right_side):
            if left_side[i] < right_side[j]:
                arr[k] = left_side[i]
                i += 1
            else:
                arr[k] = right_side[j]
                j += 1
            k += 1
            
        while i < len(left_side):
            arr[k] = left_side[i]
            i += 1
            k += 1
        while j < len(right_side):
            arr[k] = right_side[j]
            j += 1
            k += 1
    return arr

def selection_sort(arr):
    for i in range(len(arr)):
        m = i # minimum element
        for j in range(i+1,len(arr)):
            if arr[m] > arr[j]: 
                m = j
        arr[i], arr[m] = arr[m], arr[i]
    return arr

def kth(a, k): # array , k 
    n = len(a)
    m = 0
    p = (a[0] + a[-1] + a[n // 2]) // 3 # Average of "start,end and mid" element of arr
    for i in range(n):
        if a[i] > p:
            a[m], a[i] = a[i], a[m] # Swaping
            m += 1
    if k < m:
        return kth(a[:m], k)
    
    for i in range(m, n):
        if a[i] == p:
            a[m], a[i] = a[i], a[m]
            m += 1
    if k >= m:
        return kth(a[m:], k - m)
    return p

'''print("K is starts with 0 and ends with len(arr)-1")
arr = list(map(int,input("Give an array: ").split()))
k = int(input("Type K: "))
print(f"The {k}th Largest element is {kth(arr,k)}")'''

# Example usage
'''arr = [5,3,1,2,4,6]
sorted_arr = quicksort(arr)
sorted_arr_2 = insertion_sort(arr)
print("Sorted Array in Ascending Order:")
print(sorted_arr)
print(binary_search(arr, 1))
'''
arr = [1,46,3,3,5,76,42,42,43,7,67,8,63,423,42,65,8]
print(merge_sort(arr), "MERGE SORT")
print(selection_sort(arr))