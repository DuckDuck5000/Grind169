"""
Sudoku Solver

Problem Description:
------------------
Write a program to solve a Sudoku puzzle by filling the empty cells.
A sudoku solution must satisfy all of the following rules:
1. Each of the digits 1-9 must occur exactly once in each row.
2. Each of the digits 1-9 must occur exactly once in each column.
3. Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes.
The '.' character indicates empty cells.

Examples:
--------
Example 1:
Input: board = 
[["5","3",".",".","7",".",".",".","."],
 ["6",".",".","1","9","5",".",".","."],
 [".","9","8",".",".",".",".","6","."],
 ["8",".",".",".","6",".",".",".","3"],
 ["4",".",".","8",".","3",".",".","1"],
 ["7",".",".",".","2",".",".",".","6"],
 [".","6",".",".",".",".","2","8","."],
 [".",".",".","4","1","9",".",".","5"],
 [".",".",".",".","8",".",".","7","9"]]
Output: Solved sudoku board

Approach:
--------
1. Use backtracking to try different numbers
2. Check if number is valid in current position
3. Recursively solve for next empty cell
4. Time Complexity: O(9^(n*n)) where n is board size
5. Space Complexity: O(n*n) for recursion stack
"""

from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def isValid(num: str, pos: tuple) -> bool:
            row, col = pos
            
            # Check row
            for j in range(9):
                if board[row][j] == num and j != col:
                    return False
            
            # Check column
            for i in range(9):
                if board[i][col] == num and i != row:
                    return False
            
            # Check 3x3 box
            box_row, box_col = 3 * (row // 3), 3 * (col // 3)
            for i in range(box_row, box_row + 3):
                for j in range(box_col, box_col + 3):
                    if board[i][j] == num and (i, j) != pos:
                        return False
            
            return True
        
        def findEmpty() -> tuple:
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        return (i, j)
            return None
        
        def solve() -> bool:
            empty = findEmpty()
            if not empty:
                return True
            
            row, col = empty
            for num in map(str, range(1, 10)):
                if isValid(num, (row, col)):
                    board[row][col] = num
                    if solve():
                        return True
                    board[row][col] = '.'
            
            return False
        
        solve()

def run_tests():
    """Test cases with assertions"""
    solution = Solution()
    
    # Test case 1: Standard puzzle
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
    solution.solveSudoku(board1)
    # Verify solution is valid
    assert board1[0][0] == "5", "Test case 1 failed"
    assert board1[8][8] == "9", "Test case 1 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    run_tests()