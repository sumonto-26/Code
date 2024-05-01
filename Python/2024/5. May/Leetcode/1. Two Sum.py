# DATE ==> 1 May 2024
# My Logic
"""class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[i] + nums[j] == target:
                        return i, j"""
nums = list(map(int,input().split()))
val = int(input())
ans = []
for i in range(len(nums)):
    if nums[i] != val:
        ans.append(nums[i])
print(ans)