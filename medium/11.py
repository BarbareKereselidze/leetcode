"""
11. Container With Most Water

Description:
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Approach:
The idea is to use two pointers, one starting from the beginning (l) and the other from the end (r) of the array.
The width of the container is determined by the difference in indices (r - l),
and the height of the container is determined by the minimum height between the two lines (min(height[l], height[r])).

The algorithm starts with the widest container and gradually narrows it down by moving the pointers towards each other.
This ensures that the algorithm considers larger containers before narrowing down to potentially higher containers.

Complexity:
Time complexity: O(n)
Space complexity: O(1)
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        total = 0

        while l < r:
            total = max(total, min(height[l], height[r]) * (r - l))

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return total


# Example 1
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

solution1 = Solution().maxArea(height)
print(solution1)  # output -> 49

# Example 2
height = [1, 1]

solution2 = Solution().maxArea(height)
print(solution2)  # output -> 1
