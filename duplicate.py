# Given an integer array nums, return true if any value appears at 
# least twice in the array, and return false if every element is 
# distinct.
# 
# Example 1: 
# Input: nums = [1, 2, 3, 1] 
# Output: True

class Solution(object):
    
    def containsDuplicate(self, nums: list[int]) -> bool:
            num_repeated = []
            for num in nums:
                if num in num_repeated:
                    return True
                if num != num_repeated:
                    num_repeated.append(num)
            return False
        
        
def main():
    # True
    solution = Solution()
    print(f"First test: {solution.containsDuplicate([1,2,3,1])}")
    # False
    print(f"Second test: {solution.containsDuplicate([1,2,3,4])}")
    
    print(f"Third test: {solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2])}")

if __name__ == "__main__":
    main()