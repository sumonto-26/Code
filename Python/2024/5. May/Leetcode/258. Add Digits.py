num = int(input())
nums = list(str(num))
for i in range(len(nums)):
    nums[i] = int(nums[i])
while len(nums) != 1:
    nums = list(str(sum(nums)))
    for j in range(len(nums)):
        nums[j] = int(nums[j])
print(nums)