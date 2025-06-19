 """
Spiral Matrix

Problem Description:
------------------
Given an m x n matrix, return all elements of the matrix in spiral order.

Examples:
--------
Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Approach:
--------
1. Use four pointers to track boundaries: left, right, top, bottom
2. Traverse in spiral order: right → down → left → up
3. Update boundaries after each direction
4. Continue until all elements are visited
5. Time Complexity: O(m*n) where m and n are dimensions
6. Space Complexity: O(1) excluding result array
"""

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        result = []
        left, right = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1
        
        while left <= right and top <= bottom:
            # Move right
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1
            
            # Move down
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1
            
            if top <= bottom:
                # Move left
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1
            
            if left <= right:
                # Move up
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1
        
        return result

def run_tests():
    """Test cases with assertions"""
    solution = Solution()
    
    # Test case 1: 3x3 matrix
    matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
    assert solution.spiralOrder(matrix1) == [1,2,3,6,9,8,7,4,5], "Test case 1 failed"
    
    # Test case 2: 3x4 matrix
    matrix2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    assert solution.spiralOrder(matrix2) == [1,2,3,4,8,12,11,10,9,5,6,7], "Test case 2 failed"
    
    # Test case 3: Single row
    matrix3 = [[1,2,3]]
    assert solution.spiralOrder(matrix3) == [1,2,3], "Test case 3 failed"
    
    # Test case 4: Single column
    matrix4 = [[1],[2],[3]]
    assert solution.spiralOrder(matrix4) == [1,2,3], "Test case 4 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    run_tests()