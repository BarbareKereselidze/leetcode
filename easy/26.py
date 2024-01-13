"""
26. Remove Duplicates from Sorted Array

Description:
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

* Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially.
The remaining elements of nums are not important as well as the size of nums.
* Return k.

Approach:
The algorithm iterates through the array once using a while loop, removing duplicates in-place.

Complexity:
Time complexity: O(n)
Space complexity: O(1)
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 1:
            return n

        while n > 1:
            n -= 1

            if nums[n] == nums[n - 1]:
                nums.pop(n)

        return len(nums)


# Example 1
nums = [1, 1, 2]

solution1 = Solution().removeDuplicates(nums)
print(solution1)  # output -> 2, nums = [1,2,_]

# Example 2
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

solution2 = Solution().removeDuplicates(nums)
print(solution2)  # output -> 5, nums = [0,1,2,3,4,_,_,_,_,_]
