"""
Generate Parentheses

Problem Description:
------------------
Given n pairs of parentheses, write a function to generate all combinations of 
well-formed parentheses.

Examples:
--------
Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]

Approach:
--------
1. Use backtracking with two variables: open and closed parentheses count
2. Can add open parenthesis if open < n
3. Can add closed parenthesis if closed < open
4. Time Complexity: O(4^n / sqrt(n))
5. Space Complexity: O(n) for recursion stack
"""

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def backtrack(open_count: int, close_count: int, curr: str) -> None:
            # Base case: valid combination found
            if len(curr) == 2 * n:
                result.append(curr)
                return
            
            # Add open parenthesis if we have remaining ones
            if open_count < n:
                backtrack(open_count + 1, close_count, curr + "(")
            
            # Add close parenthesis if it's valid
            if close_count < open_count:
                backtrack(open_count, close_count + 1, curr + ")")
        
        result = []
        backtrack(0, 0, "")
        return result

def run_tests():
    """Test cases with assertions"""
    solution = Solution()
    
    # Test case 1: n = 3
    result1 = solution.generateParenthesis(3)
    assert len(result1) == 5, "Test case 1 failed: wrong number of combinations"
    assert "((()))" in result1, "Test case 1 failed: missing valid combination"
    
    # Test case 2: n = 1
    result2 = solution.generateParenthesis(1)
    assert result2 == ["()"], "Test case 2 failed"
    
    # Test case 3: n = 2
    result3 = solution.generateParenthesis(2)
    assert sorted(result3) == sorted(["(())", "()()"]), "Test case 3 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    run_tests()