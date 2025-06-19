"""
Letter Combinations of a Phone Number

Problem Description:
------------------
Given a string containing digits from 2-9, return all possible letter combinations
that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on telephone buttons) is:
2 -> abc
3 -> def
4 -> ghi
5 -> jkl
6 -> mno
7 -> pqrs
8 -> tuv
9 -> wxyz

Examples:
--------
Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]

Approach:
--------
1. Use backtracking with a digit-to-letters mapping
2. For each digit, try each possible letter
3. Build combinations recursively
4. Time Complexity: O(4^n) where n is length of input
5. Space Complexity: O(n) for recursion stack
"""

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        # Handle empty input
        if not digits:
            return []
        
        # Phone number mapping
        digit_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        def backtrack(index: int, curr_str: str) -> None:
            # Base case: we've processed all digits
            if index == len(digits):
                result.append(curr_str)
                return
            
            # Try each letter for current digit
            for letter in digit_map[digits[index]]:
                backtrack(index + 1, curr_str + letter)
        
        result = []
        backtrack(0, "")
        return result

def run_tests():
    """Test cases with assertions"""
    solution = Solution()
    
    # Test case 1: Two digits
    digits1 = "23"
    result1 = solution.letterCombinations(digits1)
    assert len(result1) == 9, "Test case 1 failed: wrong number of combinations"
    assert "ad" in result1, "Test case 1 failed: missing combination"
    
    # Test case 2: Empty string
    digits2 = ""
    assert solution.letterCombinations(digits2) == [], "Test case 2 failed"
    
    # Test case 3: Single digit
    digits3 = "2"
    result3 = solution.letterCombinations(digits3)
    assert sorted(result3) == ['a', 'b', 'c'], "Test case 3 failed"
    
    # Test case 4: Digits with 4 letters
    digits4 = "7"
    result4 = solution.letterCombinations(digits4)
    assert len(result4) == 4, "Test case 4 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    run_tests()