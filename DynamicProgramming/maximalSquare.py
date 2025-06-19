"""
Maximal Square

Problem Description:
------------------
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing 
only 1's and return its area.

Examples:
--------
Example 1:
Input: matrix = [
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
]
Output: 4
Explanation: The maximal square has size 2x2.

Example 2:
Input: matrix = [["0","1"],["1","0"]]
Output: 1

Approach:
--------
1. Use dynamic programming where dp[i][j] represents size of largest square ending at (i,j)
2. For each cell, if it's '1', take minimum of left, top, and diagonal neighbors plus 1
3. Keep track of maximum square size seen
4. Time Complexity: O(m*n)
5. Space Complexity: O(m*n) can be optimized to O(n)
"""

class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
            
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * (cols + 1) for _ in range(2)]  # Only need 2 rows
        max_side = 0
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == "1":
                    # Use current row and previous row of dp array
                    dp[1][j + 1] = min(dp[0][j], dp[0][j + 1], dp[1][j]) + 1
                    max_side = max(max_side, dp[1][j + 1])
                else:
                    dp[1][j + 1] = 0
            # Swap rows for next iteration
            dp[0] = dp[1][:]
        
        return max_side * max_side

def run_tests():
    """Test cases with assertions"""
    solution = Solution()
    
    # Test case 1: Regular case
    matrix1 = [
        ["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"]
    ]
    assert solution.maximalSquare(matrix1) == 4, "Test case 1 failed"
    
    # Test case 2: 2x2 matrix
    matrix2 = [["0","1"],["1","0"]]
    assert solution.maximalSquare(matrix2) == 1, "Test case 2 failed"
    
    # Test case 3: Empty matrix
    matrix3 = []
    assert solution.maximalSquare(matrix3) == 0, "Test case 3 failed"
    
    # Test case 4: All ones
    matrix4 = [["1","1"],["1","1"]]
    assert solution.maximalSquare(matrix4) == 4, "Test case 4 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    run_tests()