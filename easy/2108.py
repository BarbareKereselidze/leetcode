"""
2108. Find First Palindromic String in the Array

Description:
Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".
A string is palindromic if it reads the same forward and backward.

Approach:
The algorithm iterates through the array, checking if each element is a palindrome. If it finds a palindrome, it returns the word.
If it can't find a palindrome in the array, it returns an empty string.

Complexity:
Time complexity: O(n^2)
Space complexity: O(1)
"""

from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word == word[::-1]:
                return word
        return ""


# Example 1
words = ["abc", "car", "ada", "racecar", "cool"]

solution1 = Solution().firstPalindrome(words)
print(solution1)  # output -> "ada"

# Example 2
words = ["notapalindrome", "racecar"]

solution2 = Solution().firstPalindrome(words)
print(solution2)  # output -> "racecar"

# Example 3
words = ["def", "ghi"]

solution3 = Solution().firstPalindrome(words)
print(solution3)  # output -> ""
