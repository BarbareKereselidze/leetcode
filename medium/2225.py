"""
2225. Find Players With Zero or One Losses

Description:
You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.
Return a list answer of size 2 where:

* answer[0] is a list of all players that have not lost any matches.
* answer[1] is a list of all players that have lost exactly one match.

The values in the two lists should be returned in increasing order.

Approach:
* Create a set won_matches to store players who won at least one match
* Create a list lost_matches to store all players who lost at least one match
* Use Counter to count how many times a player lost from the lost_matches list
* Create two lists:
    lost_none: players who have not lost any matches
    lost_one: players who have lost exactly one match
* Return the sorted versions of lost_none and lost_one

Complexity:
Time complexity: O(n log(n))
Space complexity: O(n)
"""

from collections import Counter
from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        won_matches = set(pair[0] for pair in matches)
        lost_matches = [pair[1] for pair in matches]

        player_counts = Counter(lost_matches)

        lost_none = [player for player in won_matches if player_counts[player] == 0]
        lost_one = [player for player in lost_matches if player_counts[player] == 1]

        return sorted(lost_none), sorted(lost_one)


# Example 1
matches = [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]

solution1 = Solution().findWinners(matches)
print(solution1)  # output -> [[1, 2, 10], [4, 5, 7, 8]]

# Example 2
matches = [[2, 3], [1, 3], [5, 4], [6, 4]]

solution2 = Solution().findWinners(matches)
print(solution1)  # output -> [[1, 2, 5, 6], []]
