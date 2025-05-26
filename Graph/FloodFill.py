class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        original = image[sr][sc]
        if original == color:
            return image
        
        rows, cols = len(image), len(image[0])
        
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if image[r][c] != original:
                return
            image[r][c] = color
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        dfs(sr, sc)
        return image


# BFS
from collections import deque

class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        original = image[sr][sc]
        if original == color:
            return image

        rows, cols = len(image), len(image[0])
        queue = []
        queue.append((sr, sc))

        while queue:
            r, c = queue.pop(0)
            if image[r][c] == original:
                image[r][c] = color
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == original:
                        queue.append((nr, nc))
        
        return image
