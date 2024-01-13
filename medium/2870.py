"""
2870. Minimum Number of Operations to Make Array Empty

Description:
You are given a 0-indexed array nums consisting of positive integers.
There are two types of operations that you can apply on the array any number of times:
* Choose two elements with equal values and delete them from the array.
* Choose three elements with equal values and delete them from the array.
Return the minimum number of operations required to make the array empty, or -1 if it is not possible.

Approach:
The code iterates through each count of elements in the array and calculates the minimum number of operations needed.
It uses the greedy approach, trying to pair elements into operations of three, and accumulates the total operation count.

Complexity:
Time complexity: O(n + k)
Space complexity:  O(k)

where k is the number of unique elements in the input array.
"""

from collections import Counter
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operation_count = 0
        counter = Counter(nums)

        for each_count in counter.values():

            if each_count == 1:
                return -1

            operation_count += (each_count // 3 + (1 if each_count % 3 != 0 else 0))

        return operation_count


# Example 1
nums = [2, 3, 3, 2, 2, 4, 2, 3, 4]

solution1 = Solution().minOperations(nums)
print(solution1)  # output -> 4

# Example 2
nums = [2, 1, 2, 2, 3, 3]

solution2 = Solution().minOperations(nums)
print(solution2)  # output -> -1
