
a = list(map(str, input().split("+")) )


def bubble_sort(arr):

    n = len(arr)

    for i in range (n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                a = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = a
    return arr

ans = bubble_sort(a)

result = '+'.join(ans)
print(result)




