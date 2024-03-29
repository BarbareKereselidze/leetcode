"""
1347. Minimum Number of Steps to Make Two Strings Anagram

Description:
You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with another character.
Return the minimum number of steps to make t an anagram of s.
An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

Approach:
Using the Counter class from the collections module and counting the occurrences of each character in both strings, s and t.
Then calculate the difference in counts for each character and sum these differences.
This sum represents the minimum number of steps needed to make the two strings anagrams.

Complexity:
Time complexity: O(n)
Space complexity: O(n)
"""

from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_counter = Counter(s)
        t_counter = Counter(t)
        difference = sum((s_counter - t_counter).values())

        return difference


# Example 1
s = "bab"
t = "aba"

solution1 = Solution().minSteps(s, t)
print(solution1)  # output -> 1

# Example 2
s = "leetcode"
t = "practice"

solution2 = Solution().minSteps(s, t)
print(solution2)  # output -> 5

# Example 3
s = "anagram"
t = "mangaar"

solution3 = Solution().minSteps(s, t)
print(solution3)  # output -> 0
