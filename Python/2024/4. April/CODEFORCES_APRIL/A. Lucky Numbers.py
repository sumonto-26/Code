# DATE ==> 24 April 2024
# AUTHOR ==> SUMONTO

def max_diff_number(a, b):
    max_num = a
    for i in range(a, b + 1):
        diff = int(max(str(i))) - int(min(str(i)))
        if diff == 9:
            max_num = i
            break
        elif diff > 0 and diff > int(max(str(max_num))) - int(min(str(max_num))):
            max_num = i
    return max_num

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(max_diff_number(a, b))
