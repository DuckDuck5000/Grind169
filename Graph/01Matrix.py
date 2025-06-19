"""
01 Matrix

Problem Description:
------------------
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1.

Examples:
--------
Example 1:
Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
Explanation: All zeros remain zero, the 1 has zeros all around it with distance 1.

Example 2:
Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
Explanation: The closest 0 for position (2,1) is at distance 2.

Approach:
--------
1. Use BFS starting from all 0s simultaneously
2. Update distances for each 1 when visited
3. Process cells in order of increasing distance
4. Time Complexity: O(m*n)
5. Space Complexity: O(m*n)
"""

from collections import deque
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat or not mat[0]:
            return mat
            
        m, n = len(mat), len(mat[0])
        queue = deque()
        # Initialize result matrix with max value
        result = [[float('inf')] * n for _ in range(m)]
        
        # Add all 0s to queue and mark their distances as 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    result[i][j] = 0
                    queue.append((i, j))
        
        # Directions for adjacent cells
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        # Process queue
        while queue:
            row, col = queue.popleft()
            
            # Check all adjacent cells
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                
                # Check if within bounds and can update distance
                if (0 <= new_row < m and 
                    0 <= new_col < n and 
                    result[new_row][new_col] > result[row][col] + 1):
                    result[new_row][new_col] = result[row][col] + 1
                    queue.append((new_row, new_col))
        
        return result

def run_tests():
    """Test cases with assertions"""
    solution = Solution()
    
    # Test case 1: All surrounding zeros
    mat1 = [[0,0,0],
            [0,1,0],
            [0,0,0]]
    expected1 = [[0,0,0],
                 [0,1,0],
                 [0,0,0]]
    assert solution.updateMatrix(mat1) == expected1, "Test case 1 failed"
    
    # Test case 2: Multiple distances
    mat2 = [[0,0,0],
            [0,1,0],
            [1,1,1]]
    expected2 = [[0,0,0],
                 [0,1,0],
                 [1,2,1]]
    assert solution.updateMatrix(mat2) == expected2, "Test case 2 failed"
    
    # Test case 3: Single cell
    mat3 = [[0]]
    expected3 = [[0]]
    assert solution.updateMatrix(mat3) == expected3, "Test case 3 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    run_tests()