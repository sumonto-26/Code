# DATE ==> 11 MAY 2024
# AUTHOR ==> SUMONTO.

height = list(map(int,input().split(",")))
max_left = [0]
max_right = []
for l in range(1,len(height)):
    max_left.append(max(height[:l]))
    
for r in range(len(height)-1):
    max_right.append(max(height[r+1:]))
max_right.append(0)


ans_arr = []
for i in range(len(height)):
    if height[i] < min(max_left[i], max_right[i]): 
        ans_arr.append(min(max_right[i], max_left[i]) - height[i])
    else: ans_arr.append(0)

print(ans_arr)
print(sum(ans_arr))    
