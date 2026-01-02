nums = [1, 2, 3, 4, 5]

prefix = [0] * (len(nums) + 1)

#[0, 0, 0, 0, 0, 0] 

for i in range(len(nums)):
    prefix[i + 1] = prefix[i] + nums[i]

print(prefix)