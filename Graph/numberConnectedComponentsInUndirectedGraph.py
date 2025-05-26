from typing import List
from collections import defaultdict

class Solution:
    """
    LeetCode 323: Number of Connected Components in an Undirected Graph

    Given n nodes labeled from 0 to n - 1 and a list of undirected edges,
    return the number of connected components in the graph.

    We use an adjacency list (bidirectional) to represent the undirected graph.
    """

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Build bidirectional adjacency list
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        count = 0

        def dfs(node):
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)

        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i)
                count += 1

        return count