from typing import List

class Solution:
    """
    LeetCode 261: Graph Valid Tree

    Given n nodes labeled from 0 to n - 1 and a list of undirected edges,
    determine if these edges make up a valid tree.

    A valid tree must be:
      1. Connected (all nodes are reachable from any node)
      2. Acyclic (no cycles)

    Return True if the graph is a valid tree, otherwise False.
    """

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False  # A tree must have exactly n-1 edges

        parent = [i for i in range(n)]

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for u, v in edges:
            pu, pv = find(u), find(v)
            if pu == pv:
                return False  # Cycle detected
            parent[pu] = pv  # Union

        return True