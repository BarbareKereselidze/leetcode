"""
13. Roman to integer.

Description:
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
Instead, the number four is written as IV. Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9.
    X can be placed before L (50) and C (100) to make 40 and 90.
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

Approach:
The provided code is a Python implementation of a solution to convert a Roman numeral to an integer.
The algorithm utilizes a dictionary (symbols) to map each Roman numeral character to its corresponding numeric value.
It iterates through the input string s from left to right, accumulating the total integer value. It uses a special case for subtractive pairs
(e.g., IV for 4, IX for 9) by subtracting twice the previous value if the current value is greater.

Complexity:
Time complexity: O(n)
Space complexity: O(1)
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0

        symbols = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        prev_val = 0

        for value in s:
            current_val = symbols[value]
            result += current_val

            if current_val > prev_val:
                result -= 2 * prev_val

            prev_val = current_val

        return result


# Example 1
s1 = "III"
solution1 = Solution().romanToInt(s1)
print(solution1)  # Output: 3

# Example 2
s2 = "LVIII"
solution2 = Solution().romanToInt(s2)
print(solution2)  # Output: 58

# Example 3
s3 = "MCMXCIV"
solution3 = Solution().romanToInt(s3)
print(solution3)  # Output: 1994
