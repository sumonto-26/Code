a = int(input())
b = list(map(int,input().split(" ")))

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                c = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = c
    return arr

c = bubble_sort(b)
result_string = ' '.join(map(str, c))
print(result_string)
