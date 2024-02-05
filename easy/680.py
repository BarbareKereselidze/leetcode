"""
680. Valid Palindrome II


Description:
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Approach:

The code uses a recursive approach where the function valid_palindrome is called recursively to check if the given
string is a palindrome by allowing at most one character deletion. The function takes two variables l and r,
representing the left and right ends of the current substring, and a count variable,
indicating the number of characters that have been deleted.

Complexity:
Time complexity: O(n)
Space complexity: O(n)

"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        count = 1


        def valid_palindrome(l, r, count):
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    if count > 1:
                        return False
                    return valid_palindrome(l+1, r, count+1) or valid_palindrome(l, r-1, count+1)

            return True

        return valid_palindrome(l, r, count)


# Example 1
s = "aba"

solution1 = Solution().validPalindrome(s)
print(solution1)  # output -> True

# Example 2
s = "abca"

solution2 = Solution().validPalindrome(s)
print(solution2)  # output -> True

# Example 3
s = "abc"

solution3 = Solution().validPalindrome(s)
print(solution3)  # output -> False
