"""
1572. Matrix Diagonal Sum

Description:
Given a square matrix mat, return the sum of the matrix diagonals.
Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

Approach:
The code iterates through each row of the matrix and accumulates the sum by:
* adding the elements at position (i, i, primary diagonal)
* adding the elements at position (i, n - i - 1, secondary diagonal)
  if the element is not part of the primary diagonal (i is not equal to n - i - 1, where n is the size of the matrix),

Complexity:
Time complexity: O(n)
Space complexity: O(1)
"""

from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum = 0
        n = len(mat)
        for i in range(n):
            sum += mat[i][i]
            if i == n - i - 1:
                continue
            sum += mat[i][n - i - 1]
        return sum


# Example 1
mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

solution1 = Solution().diagonalSum(mat)
print(solution1)  # output -> 25

# Example 2
mat = [[1, 1, 1, 1],
       [1, 1, 1, 1],
       [1, 1, 1, 1],
       [1, 1, 1, 1]]

solution2 = Solution().diagonalSum(mat)
print(solution2)  # output -> 8

# Example 3
mat = [[5]]

solution3 = Solution().diagonalSum(mat)
print(solution3)  # output -> 5
