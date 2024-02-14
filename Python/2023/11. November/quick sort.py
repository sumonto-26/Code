def quick_sort (arr):

    if len(arr) <= 1:
        return arr

    else:
       pivot = arr[0]
       
       less = []
       for x in arr[1:]:
            if x <= pivot:
                less.append(x)

       more = [x for x in arr[1: ] if x > pivot]
       return quick_sort(less) + [pivot] + quick_sort(more)

my_list = [3,2,4,5,6,7,9,1]
print(quick_sort(my_list))



# more = [x for x in arr[1: ] if x > pivot]
