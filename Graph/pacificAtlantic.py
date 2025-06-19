from typing import List

class Solution:
    """
    LeetCode 417: Pacific Atlantic Water Flow

    Given an m x n matrix of non-negative integers representing the height of each cell,
    water can flow from a cell to another one with equal or lower height in the four directions.
    The Pacific ocean touches the left and top edges, and the Atlantic touches the right and bottom edges.
    Return a list of grid coordinates where water can flow to both the Pacific and Atlantic oceans.
    """

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r, c, visited, prev_height):
            if (
                (r, c) in visited or
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                heights[r][c] < prev_height
            ):
                return
            visited.add((r, c))
            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                dfs(r + dr, c + dc, visited, heights[r][c])

        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])

        return list(pacific & atlantic)