# def show(n):
#     if n == 0:
#         return
#     print(n)
#     show(n-1)
# show(5)


a = list(map(int,input().split()))
def my_function(a, i=0):
    if i == len(a): 
        return 1
    else:
        return a[i] * my_function(a, i + 1) 
ans1 = my_function(a)
print(f"Product == {ans1}")


def my_sum_function(a, i=0):
    if i == len(a)-1: 
        return a[i]
    else:
        return a[i] + my_sum_function(a, i + 1) 
ans2 = my_sum_function(a)
print(f"Sum == {ans2}")
