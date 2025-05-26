from typing import List

class Solution:
    """
    LeetCode 329: Longest Increasing Path in a Matrix

    Given an m x n integers matrix, find the length of the longest increasing path.
    You can move in four directions (up, down, left, right) from a cell, but only to a cell with a strictly greater value.

    This is a graph problem where each cell is a node, and edges go to strictly increasing neighbors.
    We use DFS with memoization to avoid recomputation.
    """

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        memo = [[0] * cols for _ in range(rows)]

        def dfs(r, c):
            if memo[r][c]:
                return memo[r][c]
            max_len = 1
            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                    max_len = max(max_len, 1 + dfs(nr, nc))
            memo[r][c] = max_len
            return max_len

        return max(dfs(r, c) for r in range(rows) for c in range(cols))