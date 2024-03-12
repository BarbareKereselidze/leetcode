"""
231. Power of Two

Description:
Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2x.

Approach:
The approach taken here is to repeatedly divide the given number by 2 until it becomes 1 or an odd number.
If the final result is 1, it means the original number was a power of two; otherwise, it is not.

Complexity:
Time complexity: O(log(n))
Space complexity: O(1)
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n > 0:
            if n == 1:
                return True

            if n % 2 != 0:
                break
            n //= 2

        return False


# Example 1
n = 1

solution1 = Solution().isPowerOfTwo(n)
print(solution1)  # output -> True

# Example 2
n = 16

solution2 = Solution().isPowerOfTwo(n)
print(solution2)  # output -> True

# Example 3
n = 3

solution3 = Solution().isPowerOfTwo(n)
print(solution3)  # output -> False
