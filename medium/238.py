"""
238. Product of Array Except Self

Description:
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Approach:
The algorithm uses two passes through the input array to calculate the product of all elements to the left and right of each element.
It then combines these left and right products to get the final result.
* In the first pass, iterate from the second element to the end of the array, updating new_nums to store the product of elements to the left of the current element.
* In the second pass, iterate from the second-to-last element to the beginning of the array,
  updating new_nums to include the product of elements to the right of the current element and updating r accordingly.

Complexity:
Time complexity: O(n)
Space complexity: O(1)
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        new_nums = [1] * n

        for i in range(1, n):
            new_nums[i] = new_nums[i-1] * nums[i-1]

        r = nums[-1]
        for i in range(n - 2, -1, -1):
            new_nums[i] *= r
            r *= nums[i]

        return new_nums


# Example 1
nums = [1, 2, 3, 4]

solution1 = Solution().productExceptSelf(nums)
print(solution1)  # output -> [24, 12, 8, 6]

# Example 2
nums = [-1, 1, 0, -3, 3]

solution2 = Solution().productExceptSelf(nums)
print(solution2)  # output -> [0, 0, 9, 0, 0]
