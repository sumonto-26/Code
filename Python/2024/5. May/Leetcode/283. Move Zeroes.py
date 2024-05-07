# DATE ==> 5 May 2024

nums = list(map(int,input().split()))
for i in range(nums.count(0)):
    nums.remove(0)
    nums.append(0)
    
print(nums)