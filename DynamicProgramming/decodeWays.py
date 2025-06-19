"""
Decode Ways

Problem Description:
------------------
A message containing letters from A-Z can be encoded into numbers using: 'A' -> "1"
through 'Z' -> "26". Given a string s containing only digits, return the number of ways
to decode it.

Examples:
--------
Example 1:
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12)

Example 2:
Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6)

Example 3:
Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because "6" is different from "06"

Approach:
--------
1. Use dynamic programming with space optimization
2. For each digit, consider:
   - Single digit decode if digit is not '0'
   - Two digit decode if previous two digits form valid number (10-26)
3. Time Complexity: O(n)
4. Space Complexity: O(1)
"""

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        
        # dp[i] represents number of ways to decode string ending at i
        two_back = 1  # Empty string has 1 way
        one_back = 1  # First digit if valid
        
        for i in range(1, len(s)):
            current = 0
            
            # Single digit decode
            if s[i] != '0':
                current += one_back
            
            # Two digit decode
            two_digit = int(s[i-1:i+1])
            if 10 <= two_digit <= 26:
                current += two_back
            
            # Update pointers
            two_back = one_back
            one_back = current
        
        return one_back

def run_tests():
    """Test cases with assertions"""
    solution = Solution()
    
    # Test case 1: Multiple ways to decode
    assert solution.numDecodings("12") == 2, "Test case 1 failed"
    
    # Test case 2: Three ways to decode
    assert solution.numDecodings("226") == 3, "Test case 2 failed"
    
    # Test case 3: Invalid leading zero
    assert solution.numDecodings("06") == 0, "Test case 3 failed"
    
    # Test case 4: Single digit
    assert solution.numDecodings("9") == 1, "Test case 4 failed"
    
    # Test case 5: Multiple zeros
    assert solution.numDecodings("1201") == 1, "Test case 5 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    run_tests()