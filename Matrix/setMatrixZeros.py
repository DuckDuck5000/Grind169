
from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        cols = {}
        rows = {}
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if matrix[i][j] == 0:
                    cols[j] = 1
                    rows[i] = 1
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if i in rows or j in cols:
                    matrix[i][j] = 0
def run_tests():
    """Test cases with assertions"""
    solution = Solution()
    
    # Test case 1: Basic case
    matrix1 = [[1,1,1],[1,0,1],[1,1,1]]
    solution.setZeroes(matrix1)
    assert matrix1 == [[1,0,1],[0,0,0],[1,0,1]], "Test case 1 failed"
    
    # Test case 2: Multiple zeros
    matrix2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    solution.setZeroes(matrix2)
    assert matrix2 == [[0,0,0,0],[0,4,5,0],[0,3,1,0]], "Test case 2 failed"
    
    # Test case 3: First row and column zeros
    matrix3 = [[1,0,3],[0,5,6],[7,8,9]]
    solution.setZeroes(matrix3)
    assert matrix3 == [[0,0,0],[0,0,6],[0,0,9]], "Test case 3 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    run_tests()
                    
        