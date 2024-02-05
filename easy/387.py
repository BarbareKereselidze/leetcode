"""
387. First Unique Character in a String

Description:
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Approach:
The approach is to iterate through the lowercase English letters and, for each letter, check if it appears only once in
the given string s. If a letter appears only once, store its index in a list. Finally, return the minimum index from the list,
indicating the position of the first non-repeating character. If no such character exists, return -1.

Complexity:
Time complexity: O(n^2)
Space complexity: O(n)

"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        letters = 'abcdefghijklmnopqrstuvwxyz'
        ind_list = []

        for letter in letters:
            if s.count(letter) == 1:
                ind_list.append(s.find(letter))

        if not ind_list:
            return -1
        else:
            return min(ind_list)


# Example 1
s = "leetcode"

solution1 = Solution().firstUniqChar(s)
print(solution1)  # output -> 0

# Example 2
s = "loveleetcode"

solution2 = Solution().firstUniqChar(s)
print(solution2)  # output -> 2

# Example 3
s = "aabb"

solution3 = Solution().firstUniqChar(s)
print(solution3)  # output -> -1
