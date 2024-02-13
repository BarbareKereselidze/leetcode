"""
961. N-Repeated Element in Size 2N Array

Description:
You are given an integer array nums with the following properties:
    nums.length == 2 * n.
    nums contains n + 1 unique elements.
    Exactly one element of nums is repeated n times.
Return the element that is repeated n times.

Approach:
The algorithm iterates through the array, checking if each element is in the array twice or more times.
If it finds such element it returns the element that is repeated n times.
If not it returns -1.

Complexity:
Time complexity: O(n^2)
Space complexity: O(1)
"""

from typing import List


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        for num in nums:
            if nums.count(num) >= 2:
                return num
        return -1


# Example 1
nums = [1, 2, 3, 3]

solution1 = Solution().repeatedNTimes(nums)
print(solution1)  # output -> "3

# Example 2
nums = [2, 1, 2, 5, 3, 2]

solution2 = Solution().repeatedNTimes(nums)
print(solution2)  # output -> 2

# Example 3
nums = [5, 1, 5, 2, 5, 3, 5, 4]

solution3 = Solution().repeatedNTimes(nums)
print(solution3)  # output -> 5