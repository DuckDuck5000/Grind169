"""
Minimum Height Trees

Problem Description:
------------------
Given a tree of n nodes labeled from 0 to n-1, and an array of n-1 edges where 
edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi,
find all the centroids of the tree. Return an array of all possible centroids.

A centroid is a node where, if we make it the root of the tree, the resulting tree has 
minimum height (MHT).

Examples:
--------
Example 1:
Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]
Explanation: The tree looks like:
    0
    |
    1
   / \
  2   3
Choosing node 1 as root gives minimum height of 1.

Example 2:
Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
Output: [3,4]
Explanation: Choosing either node 3 or 4 as root gives minimum height of 2.

Approach:
--------
1. Use topological sort starting from leaves
2. Remove leaves level by level until 1 or 2 nodes remain
3. The remaining nodes are the centroids
4. Time Complexity: O(n)
5. Space Complexity: O(n)
"""

from collections import defaultdict, deque
from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return list(range(n))
            
        # Build adjacency list
        adj = defaultdict(set)
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)
            
        # Start with leaves (nodes with degree 1)
        leaves = deque([node for node in range(n) if len(adj[node]) == 1])
        
        remaining_nodes = n
        # Remove leaves until 1 or 2 nodes remain
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            new_leaves = deque()
            
            # Process current level of leaves
            for leaf in leaves:
                # Get the only neighbor
                neighbor = adj[leaf].pop()
                # Remove leaf from neighbor's adjacency list
                adj[neighbor].remove(leaf)
                # If neighbor becomes leaf, add to next level
                if len(adj[neighbor]) == 1:
                    new_leaves.append(neighbor)
                    
            leaves = new_leaves
            
        return list(leaves)

def run_tests():
    """Test cases with assertions"""
    solution = Solution()
    
    # Test case 1: Single centroid
    n1, edges1 = 4, [[1,0],[1,2],[1,3]]
    assert solution.findMinHeightTrees(n1, edges1) == [1], "Test case 1 failed"
    
    # Test case 2: Two centroids
    n2, edges2 = 6, [[3,0],[3,1],[3,2],[3,4],[5,4]]
    result2 = solution.findMinHeightTrees(n2, edges2)
    assert sorted(result2) == [3,4], "Test case 2 failed"
    
    # Test case 3: Two nodes
    n3, edges3 = 2, [[0,1]]
    result3 = solution.findMinHeightTrees(n3, edges3)
    assert sorted(result3) == [0,1], "Test case 3 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    run_tests()