"""
1828. Queries on Number of Points Inside a Circle

Description:
You are given an array points where points[i] = [xi, yi] is the coordinates of the ith point on a 2D plane. Multiple points can have the same coordinates.
You are also given an array queries where queries[j] = [xj, yj, rj] describes a circle centered at (xj, yj) with a radius of rj.
For each query queries[j], compute the number of points inside the jth circle. Points on the border of the circle are considered inside.
Return an array answer, where answer[j] is the answer to the jth query.

Approach:
For each circle described in the queries list, iterate over all points in the points list.
For each point, calculate the squared distance between the point and the center of the circle using the distance formula.
If this distance is less than or equal to the square of the radius of the circle, consider the point to be inside the circle.
Count the number of points that satisfy the condition for each circle and append the count to the result list.

Complexity:
Time complexity: O(n^2)
Space complexity: O(n)
"""

from typing import List


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:

        lst = []

        for circle in queries:
            x2, y2, r = circle
            count = 0

            for point in points:
                x1, y1 = point
                distance = (x2 - x1) ** 2 + (y2 - y1) ** 2
                if distance <= r ** 2:
                    count += 1

            lst.append(count)

        return lst


# Example 1
points = [[1, 3], [3, 3], [5, 3], [2, 2]]
queries = [[2, 3, 1], [4, 3, 1], [1, 1, 2]]
solution1 = Solution().countPoints(points, queries)
print(solution1)  # Output: [3, 2, 2]


# Example 2
points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
queries = [[1, 2, 2], [2, 2, 2], [4, 3, 2], [4, 3, 3]]
solution2 = Solution().countPoints(points, queries)
print(solution2)  # Output: [2, 3, 2, 4]

