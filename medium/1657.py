"""
1657. Determine if Two Strings Are Close

Description:
Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
    For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
    For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)

You can use the operations on either string as many times as necessary.
Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

Approach:
The provided algorithm checks if two strings, word1 and word2, are considered close based on the given operations
(swapping characters and transforming occurrences of one character into another).
The algorithm checks if:
* length of wor1 and word2 are equal
* characters of word1 and word2 are the same
* the count of characters in word1 and word2 are equal to each other

Complexity:
Time complexity: O(n^2)
Space complexity: O(n)
"""


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) == len(word2):
            set1 = set(word1)
            set2 = set(word2)
            if set1 == set2:
                char_count1 = [word1.count(char) for char in set1]
                char_count2 = [word2.count(char) for char in set2]
                if sorted(char_count1) == sorted(char_count2):
                    return True


# Example 1
word1 = "abc"
word2 = "bca"

solution1 = Solution().closeStrings(word1, word2)
print(solution1)  # output -> true

# Example 2
word1 = "a"
word2 = "aa"

solution2 = Solution().closeStrings(word1, word2)
print(solution1)  # output -> false

# Example 1
word1 = "cabbba"
word2 = "abbccc"

solution1 = Solution().closeStrings(word1, word2)
print(solution1)  # output -> true
