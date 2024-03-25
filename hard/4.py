"""
4. Median of Two Sorted Arrays

Description:
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Approach:
The approach used here is to merge the two sorted arrays into a single sorted array and then
find the median of this merged array. To merge the arrays, we concatenate them and then sort the resulting array.
Finally, we calculate the median based on whether the length of the merged array is even or odd.

Complexity:
Time complexity: O((m + n) log(m + n))
Space complexity: O(m + n)
"""

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_nums = nums1 + nums2
        new_nums.sort()

        nums_len = len(new_nums)

        if nums_len % 2 == 0:
            return (new_nums[int(nums_len / 2)] + new_nums[int(nums_len / 2 - 1)]) / 2
        else:
            return new_nums[nums_len // 2]


# Example 1
nums1 = [1, 3]
nums2 = [2]

solution1 = Solution().findMedianSortedArrays(nums1, nums2)
print(solution1)  # output -> 2

# Example 2
nums1 = [1, 2]
nums2 = [3, 4]

solution2 = Solution().findMedianSortedArrays(nums1, nums2)
print(solution2)  # output -> 2.5
