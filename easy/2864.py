"""
2864. Maximum Odd Binary Number

Description:
You are given a binary string s that contains at least one '1'.
You have to rearrange the bits in such a way that the resulting binary number is the maximum
odd binary number that can be created from this combination.
Return a string representing the maximum odd binary number that can be created from the given combination.
Note that the resulting string can have leading zeros.

Approach:
Count the number of '1's in the input binary string. Construct the output string by placing '1's equal to
the count of '1's minus one (ensuring the resulting number is odd),
followed by '0's to fill the remaining length of the string, and ending with a '1'.

Complexity:
Time complexity: O(n)
Space complexity: O(n)
"""


class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        one_count = s.count("1")

        return "1" * (one_count - 1) + "0" * (len(s) - one_count) + "1"


# Example 1
s = "010"

solution1 = Solution().maximumOddBinaryNumber(s)
print(solution1)  # output -> "001"

# Example 2
s = "0101"

solution2 = Solution().maximumOddBinaryNumber(s)
print(solution2)  # output -> "1001"
