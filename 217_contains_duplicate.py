#Given an integer array nums, return true if any value 
# appears at least twice in the array, and return false if every 
# element is distinct. e.g 
# Input: nums = [1, 2, 4, 1]
# Output: True

nums = [1, 2, 4, 1]
nums_2 = [1, 2, 3, 4, 5]

def contains_duplicate(nums: list) -> bool:
        N = len(nums)
        seen = {}
        for i in range(N):
            if nums[i] in seen:
                return True
            else:
                seen[nums[i]] = i
        return False
    
print(contains_duplicate(nums))
print(contains_duplicate(nums_2))