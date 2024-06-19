# DATE ==> 19 JUNE 2024
# AUTHOR ==> SUMONTO
def merge_sort1(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort1(left_half)
        merge_sort1(right_half)
        i = j = k = 0
        while(i<len(left_half) and j< len(right_half)):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while (i<len(left_half)):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while (j<len(right_half)):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

def merge_sort2(arr):
    if len(arr) > 1:
        # DIVIDEING
        mid = len(arr)//2
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort2(left_half)
        merge_sort2(right_half)
        
        # MERGING
        i = j = k = 0
        while( i < len(left_half) and j < len(right_half)):
            if left_half[i] < right_half[j]:  # MOST IMPORTANT LINE
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
    return arr

def merge_sort3(a):
    if len(a) > 1:
        l = a[:len(a)//2]
        r = a[len(a)//2:]
        merge_sort3(l)
        merge_sort3(r)
        
        i = j = k = 0
        while(i < len(l) and j < len(r)):
            if l[i] > r[j]:
                a[k] = l[i]
                i += 1
            else:
                a[k] = r[j]
                j += 1
            k += 1
        while(i < len(l)):
            a[k] = l[i]
            i += 1
            k += 1
        while(j < len(r)):
            a[k] = r[j]
            j += 1
            k += 1
    return a

def merge_sort4(a):
    if len(a) > 1:
        m = len(a)//2
        l = a[:m]
        r = a[m:]
        merge_sort4(l)
        merge_sort4(r)
        
        i = j = k = 0
        x,y = len(l), len(r)
        while (i < x and j < y):
            if l[i] > r[j]:
                a[k] = l[i]
                i += 1
            else:
                a[k] = r[j]
                j += 1
            k += 1
        while(i < x):
            a[k] = l[i]
            i += 1
            k += 1
        while(j < y):
            a[k] = r[j]
            j += 1
            k += 1
    return a

arr = list(map(int,input().split()))
print(merge_sort1(arr))
print(merge_sort2(arr))
print(merge_sort3(arr))
print(merge_sort4(arr))