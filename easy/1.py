"""
1. Two Sum

Description:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Approach:
The algorithm iterates through the array, checking each element and their complement element
if there is a complement (target - current element) in the remaining part of the array, it returns the indices of the two numbers.

Complexity:
Time complexity: O(n^2)
Space complexity: O(1)
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            complement = target - num

            if complement in nums[i + 1:]:
                return [i, nums.index(complement, i + 1)]


# Example 1
nums = [2, 7, 11, 15]
target = 9

solution1 = Solution().twoSum(nums, target)
print(solution1)  # output -> [0, 1]

# Example 2
nums = [3, 2, 4]
target = 6

solution2 = Solution().twoSum(nums, target)
print(solution2)  # output -> [1, 2]

# Example 3
nums = [3, 3]
target = 6

solution3 = Solution().twoSum(nums, target)
print(solution3)  # output -> [0, 1]
