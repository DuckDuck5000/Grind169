"""
N-Queens

Problem Description:
------------------
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that
no two queens threaten each other. Given an integer n, return all distinct solutions to
the n-queens puzzle. Each solution contains a distinct board configuration of the n-queens'
placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

Examples:
--------
Example 1:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle

Example 2:
Input: n = 1
Output: [["Q"]]

Approach:
--------
1. Use backtracking to try placing queens row by row
2. Keep track of columns, diagonals, and anti-diagonals
3. Build board configuration when valid solution found
4. Time Complexity: O(n!)
5. Space Complexity: O(n) for recursion stack
"""

class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        def create_board() -> list[str]:
            board = []
            for row in queens:
                board_row = ['.' for _ in range(n)]
                board_row[row] = 'Q'
                board.append(''.join(board_row))
            return board
        
        def backtrack(row: int) -> None:
            if row == n:
                result.append(create_board())
                return
            
            for col in range(n):
                if col in columns or \
                   (row + col) in positive_diagonals or \
                   (row - col) in negative_diagonals:
                    continue
                    
                # Place queen
                queens[row] = col
                columns.add(col)
                positive_diagonals.add(row + col)
                negative_diagonals.add(row - col)
                
                # Try next row
                backtrack(row + 1)
                
                # Remove queen (backtrack)
                columns.remove(col)
                positive_diagonals.remove(row + col)
                negative_diagonals.remove(row - col)
        
        result = []
        queens = [0] * n  # queens[row] = column
        columns = set()
        positive_diagonals = set()  # row + col
        negative_diagonals = set()  # row - col
        
        backtrack(0)
        return result

def run_tests():
    """Test cases with assertions"""
    solution = Solution()
    
    # Test case 1: n = 4
    result1 = solution.solveNQueens(4)
    assert len(result1) == 2, "Test case 1 failed: wrong number of solutions"
    
    # Test case 2: n = 1
    result2 = solution.solveNQueens(1)
    assert result2 == [["Q"]], "Test case 2 failed"
    
    # Test case 3: n = 2 (no solutions)
    result3 = solution.solveNQueens(2)
    assert len(result3) == 0, "Test case 3 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    run_tests()