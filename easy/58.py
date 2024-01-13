"""
58. Length of Last Word

Description:
Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.

Approach:
The code uses the split() method to separate the words in the string by spaces.
It then takes the last element of the resulting list to get the last word and returns its length.

Complexity:
Time complexity: O(n)
Space complexity: O(number of words)
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])


# Example 1
s = "Hello World"

solution1 = Solution().lengthOfLastWord(s)
print(solution1)  # output -> 5

# Example 2
s = "   fly me   to   the moon  "

solution2 = Solution().lengthOfLastWord(s)
print(solution2)  # output -> 4

# Example 3
s = "luffy is still joyboy"

solution3 = Solution().lengthOfLastWord(s)
print(solution3)  # output -> 6
