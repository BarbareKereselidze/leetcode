"""
42. Trapping Rain Water

Description:
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Approach:
The code is using a two-pointer approach to iterate through the elevation map and calculate the trapped water.
It identifies local maximums, and for each pair of consecutive local maximums, it calculates the trapped water by iterating
through the elements in between.

Complexity:
Time complexity:  O(n^2)
Space complexity: O(1)
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        trapped = 0

        first_ind = 0
        while first_ind < (n - 1):

            max_ind = max(height[first_ind:])
            max_ind_count = height[first_ind:].count(max_ind)

            if height[first_ind] == max_ind and max_ind_count == 1:
                height[first_ind:] = height[first_ind:][::-1]

            second_ind = first_ind + 1

            while second_ind < n and height[second_ind] < height[first_ind]:
                second_ind += 1

            if second_ind == n:
                break

            min_height = min(height[second_ind], height[first_ind])
            for i in range(first_ind + 1, second_ind):
                trapped += (min_height - height[i])

            first_ind = second_ind

        return trapped


# Example 1
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

solution1 = Solution().trap(height)
print(solution1)  # output -> 6

# Example 2
height = [4, 2, 0, 3, 2, 5]

solution2 = Solution().trap(height)
print(solution2)  # output -> 9
