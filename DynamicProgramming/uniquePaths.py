"""
Unique Paths

Problem Description:
------------------
There is a robot on an m x n grid. The robot can only move either down or right at any point.
The robot is trying to reach the bottom-right corner of the grid.
How many possible unique paths are there?

Examples:
--------
Example 1:
Input: m = 3, n = 7
Output: 28
Explanation: From top-left corner, robot can reach bottom-right through 28 different paths

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation: From top-left corner, all possible paths are:
1. Right -> Down -> Down
2. Down -> Right -> Down
3. Down -> Down -> Right

Approach:
--------
1. Use 2D dynamic programming (can be optimized to 1D)
2. Each cell represents number of ways to reach that cell
3. dp[i][j] = dp[i-1][j] + dp[i][j-1]
4. Time Complexity: O(m * n)
5. Space Complexity: O(n) with space optimization
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize 1D dp array
        dp = [1] * n
        
        # Calculate paths for each row
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j-1]
        
        return dp[n-1]

def run_tests():
    """Test cases with assertions"""
    solution = Solution()
    
    # Test case 1: 3x7 grid
    assert solution.uniquePaths(3, 7) == 28, "Test case 1 failed"
    
    # Test case 2: 3x2 grid
    assert solution.uniquePaths(3, 2) == 3, "Test case 2 failed"
    
    # Test case 3: 1x1 grid
    assert solution.uniquePaths(1, 1) == 1, "Test case 3 failed"
    
    # Test case 4: 3x3 grid
    assert solution.uniquePaths(3, 3) == 6, "Test case 4 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    run_tests()