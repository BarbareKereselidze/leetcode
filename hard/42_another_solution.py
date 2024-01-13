"""
42. Trapping Rain Water

Description:
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Approach:
The code is using a two-pointer approach to iterate through the elevation map and calculate the trapped water.
The code basically goes through layers of water. It calculates how much water would be on the first layer and goes on until it find the last layer where it stops.
l and r are used to find the first elements from left and right, which is higher than the layer of water we are on.
On each layer we find water that is trapped between l and r.

Complexity:
Time complexity: O(n^2)
Space complexity: O(1)
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        count = 0
        height_len = len(height)
        i = 0

        while True:
            l = None
            r = None

            for j in range(height_len):
                if l is None:
                    if height[j] > i:
                        l = j

                if r is None:
                    ind = height_len - j - 1
                    if height[ind] > i:
                        r = ind

            if l == r:
                break

            if i-1 in height[l:r]:
                height[l:r] = [i if x == i-1 else x for x in height[l:r]]

            if i in height[l:r]:
                count += height[l:r].count(i)

            i += 1
        return count


# Example 1
height1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

solution1 = Solution().trap(height1)
print(solution1)  # output -> 6

# Example 2
height2 = [4, 2, 0, 3, 2, 5]

solution2 = Solution().trap(height2)
print(solution2)  # output -> 9
