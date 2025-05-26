from collections import deque

class Solution:
    """
    LeetCode 1197: Minimum Knight Moves

    Given an infinite chessboard, a knight starts at (0, 0) and needs to reach (x, y).
    Return the minimum number of moves required for the knight to reach the target.

    Graph theory applies here because each position on the chessboard is a node,
    and each valid knight move is an edge to another node. The problem is to find
    the shortest path (minimum moves) from the start node to the target node,
    which is a classic Breadth-First Search (BFS) problem on an unweighted graph.
    """

    def minKnightMoves(self, x: int, y: int) -> int:
        # Use symmetry to reduce the search space
        x, y = abs(x), abs(y)
        directions = [
            (2, 1), (1, 2), (-1, 2), (-2, 1),
            (-2, -1), (-1, -2), (1, -2), (2, -1)
        ]
        visited = set()
        queue = deque([(0, 0, 0)])  # (row, col, moves)

        while queue:
            r, c, moves = queue.popleft()
            if (r, c) == (x, y):
                return moves
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # Only consider positions in the first quadrant due to symmetry
                if (nr, nc) not in visited and nr >= -2 and nc >= -2:
                    visited.add((nr, nc))
                    queue.append((nr, nc, moves + 1))
        return -1