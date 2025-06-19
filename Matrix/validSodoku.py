"""
Valid Sudoku

Problem Description:
------------------
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated
according to the following rules:
1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3 x 3 sub-boxes must contain digits 1-9 without repetition.

Examples:
--------
Example 1:
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Approach:
--------
1. Use sets to track numbers in each row, column, and 3x3 box
2. Check each filled cell against all three rules
3. Use box_id formula to identify which 3x3 box a cell belongs to
4. Time Complexity: O(1) since board is always 9x9
5. Space Complexity: O(1) for fixed size sets
"""

from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialize sets to track numbers
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        # Check each cell
        for i in range(9):
            for j in range(9):
                # Skip empty cells
                if board[i][j] == '.':
                    continue
                    
                num = board[i][j]
                box_id = (i // 3) * 3 + j // 3
                
                # Check if number already exists
                if (num in rows[i] or 
                    num in cols[j] or 
                    num in boxes[box_id]):
                    return False
                
                # Add number to sets
                rows[i].add(num)
                cols[j].add(num)
                boxes[box_id].add(num)
        
        return True

def run_tests():
    """Test cases with assertions"""
    solution = Solution()
    
    # Test case 1: Valid Sudoku
    board1 = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    assert solution.isValidSudoku(board1), "Test case 1 failed"
    
    # Test case 2: Invalid row
    board2 = [
        ["5","3",".",".","7",".","5",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    assert not solution.isValidSudoku(board2), "Test case 2 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    run_tests()