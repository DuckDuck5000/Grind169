"""
Rotate Image

Problem Description:
------------------
You are given an n x n 2D matrix representing an image. Rotate the image by 90 degrees
clockwise. You have to rotate the image in-place, which means you have to modify the
input 2D matrix directly without using another 2D matrix.

Examples:
--------
Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Approach:
--------
1. First transpose the matrix (swap elements across diagonal)
2. Then reverse each row
3. This effectively rotates the matrix 90 degrees clockwise
4. Time Complexity: O(n²) where n is the size of matrix
5. Space Complexity: O(1) as we modify in-place
"""

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        
        # Step 1: Transpose matrix
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Step 2: Reverse each row
        for i in range(n):
            left, right = 0, n-1
            while left < right:
                matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
                left += 1
                right -= 1

def run_tests():
    """Test cases with assertions"""
    solution = Solution()
    
    # Test case 1: 3x3 matrix
    matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
    solution.rotate(matrix1)
    assert matrix1 == [[7,4,1],[8,5,2],[9,6,3]], "Test case 1 failed"
    
    # Test case 2: 4x4 matrix
    matrix2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    solution.rotate(matrix2)
    assert matrix2 == [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]], "Test case 2 failed"
    
    # Test case 3: 1x1 matrix
    matrix3 = [[1]]
    solution.rotate(matrix3)
    assert matrix3 == [[1]], "Test case 3 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    run_tests()