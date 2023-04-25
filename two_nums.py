# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


class Solution(object):
    
    def twoSum(self, nums: list[int], target: int) -> list:
            elements_seen = {}
            for i in range(len(nums)):

                difference = target - nums[i]
                print(f"{i}, {nums[i]}, {difference}, {target}")
                if difference in elements_seen:
                    return [elements_seen[difference], i]
                else:
                    elements_seen[nums[i]] = i
                    print(f"elements seen, {elements_seen}")    


def main():
    solution = Solution()
    # print(solution.twoSum([2, 7, 11, 15], 9)) # [0, 1]
    # print(solution.twoSum([2, 4, 9, 6, 5], 10)) # [1, 3]
    # print(solution.twoSum([3, 5, 9, 2, 0, 2, 8, 1, 7], 4)) # [3, 5]
    print(solution.twoSum([2, 7, 5, 8], 7)) # [0, 2]
    
if __name__ == "__main__":
    main()