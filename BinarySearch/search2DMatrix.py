class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1
        
        while left <= right:
            mid = (left + right) // 2
            # Convert 1D index to 2D coordinates
            row = mid // cols
            col = mid % cols
            value = matrix[row][col]
            
            if value == target:
                return True
            elif value < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Target exists in matrix
    matrix1 = [
        [1,3,5,7],
        [10,11,16,20],
        [23,30,34,60]
    ]
    target1 = 3
    result1 = solution.searchMatrix(matrix1, target1)
    assert result1 == True, f"Expected True but got {result1}"
    
    # Test case 2: Target doesn't exist
    target2 = 13
    result2 = solution.searchMatrix(matrix1, target2)
    assert result2 == False, f"Expected False but got {result2}"
    
    # Test case 3: Empty matrix
    matrix2 = []
    target3 = 1
    result3 = solution.searchMatrix(matrix2, target3)
    assert result3 == False, f"Expected False but got {result3}"
    
    # Test case 4: Single element matrix
    matrix3 = [[1]]
    target4 = 1
    result4 = solution.searchMatrix(matrix3, target4)
    assert result4 == True, f"Expected True but got {result4}"
    
    print("All test cases passed!")