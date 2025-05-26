from typing import List
from collections import deque

class Solution:
    """
    LeetCode 1730: Shortest Path to Get Food

    Given a grid of characters where:
      - '*' is your starting position (exactly one)
      - '#' is a food cell (at least one)
      - 'O' is an open cell you can walk on
      - 'X' is a blocked cell you cannot walk on

    Return the minimum number of steps to reach any food cell from the starting position.
    If it is not possible, return -1.
    """

    def getFood(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        queue = deque()

        # Find the starting position
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '*':
                    queue.append((r, c, 0))  # (row, col, steps)
                    visited[r][c] = True

        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        while queue:
            r, c, steps = queue.popleft()
            if grid[r][c] == '#':
                return steps
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < rows and
                    0 <= nc < cols and
                    not visited[nr][nc] and
                    grid[nr][nc] != 'X'
                ):
                    visited[nr][nc] = True
                    queue.append((nr, nc, steps + 1))
        return -1