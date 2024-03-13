# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they 
# add up to target.

# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.

# You can return the answer in any order


nums, target = [2, 7, 11, 15], 9
nums_2, target_2 = [1, 2, 3, 4], 8

def two_sum(nums: list, target) -> list:
    seen = {}
    N = len(nums)
    for i in range(N):
        difference = target - nums[i]
        if difference in seen:
            return [seen[difference], i]
        else:
            seen[nums[i]] = i
    return []
     
print(two_sum(nums, target))
print(two_sum(nums_2, target_2))
     