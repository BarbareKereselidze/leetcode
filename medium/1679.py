"""
1679. Max Number of K-Sum Pairs

Description:
You are given an integer array nums and an integer k.
In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
Return the maximum number of operations you can perform on the array.

Approach:
The approach used in the code is a two-pointer approach. The array nums is first sorted, and then two pointers (l and r)
are initialized at the beginning and the end of the sorted array. The algorithm iterates through the array, and in each iteration,
it checks the sum of the elements at the current positions of the pointers.

* If the sum is greater than k, it means the current pair is too large, so the right pointer (r) is moved one position to the left.
* If the sum is less than k, it means the current pair is too small, so the left pointer (l) is moved one position to the right.
* If the sum is equal to k, it means a valid pair is found, and both pointers are moved towards each other. The count of valid pairs is incremented.

Complexity:
Time complexity: O(n * log(n))
Space complexity: O(1)
"""

from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        l = 0
        r = len(nums) - 1
        count = 0

        nums.sort()

        while l < r:
            if nums[l] + nums[r] > k:
                r -= 1
            elif nums[l] + nums[r] < k:
                l += 1
            else:
                l += 1
                r -= 1
                count += 1

        return count


# Example 1
nums = [1, 2, 3, 4]
k = 5

solution1 = Solution().maxOperations(nums, k)
print(solution1)  # output -> 2

# Example 2
nums = [3, 1, 3, 4, 3]
k = 6

solution2 = Solution().maxOperations(nums, k)
print(solution2)  # output -> 1
