"""
All Nodes Distance K in Binary Tree

Problem Description:
------------------
Given the root of a binary tree, the value of a target node target, and an integer k, 
return an array of the values of all nodes that have a distance k from the target node.

Examples:
--------
Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes with values 7, 4, and 1 are at distance 2 from target node 5

Example 2:
Input: root = [1], target = 1, k = 3
Output: []

Approach:
--------
1. Convert tree to undirected graph using parent pointers
2. Use BFS to find nodes at distance k from target
3. Use set to track visited nodes
4. Time Complexity: O(n) where n is number of nodes
5. Space Complexity: O(n) for graph and queue
"""

from typing import List, Optional
from collections import defaultdict, deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # Build graph with parent pointers
        def build_graph(node: TreeNode, parent: TreeNode) -> None:
            if not node:
                return
            
            if parent:
                graph[node].append(parent)
                graph[parent].append(node)
            
            build_graph(node.left, node)
            build_graph(node.right, node)
        
        # Create adjacency list representation
        graph = defaultdict(list)
        build_graph(root, None)
        
        # BFS to find nodes at distance k
        queue = deque([(target, 0)])  # (node, distance)
        visited = {target}
        result = []
        
        while queue:
            node, dist = queue.popleft()
            
            # If we found a node at distance k, add to result
            if dist == k:
                result.append(node.val)
                continue
            
            # Add unvisited neighbors
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, dist + 1))
        
        return result

def run_tests():
    """Test cases with assertions"""
    solution = Solution()
    
    # Test case 1: Regular tree
    root1 = TreeNode(3)
    root1.left = TreeNode(5)
    root1.right = TreeNode(1)
    root1.left.left = TreeNode(6)
    root1.left.right = TreeNode(2)
    root1.right.left = TreeNode(0)
    root1.right.right = TreeNode(8)
    root1.left.right.left = TreeNode(7)
    root1.left.right.right = TreeNode(4)
    
    result1 = solution.distanceK(root1, root1.left, 2)
    assert sorted(result1) == sorted([7,4,1]), "Test case 1 failed"
    
    # Test case 2: Single node
    root2 = TreeNode(1)
    assert solution.distanceK(root2, root2, 1) == [], "Test case 2 failed"
    
    # Test case 3: Nodes only in one direction
    root3 = TreeNode(1)
    root3.left = TreeNode(2)
    root3.left.left = TreeNode(3)
    result3 = solution.distanceK(root3, root3.left, 1)
    assert sorted(result3) == sorted([1,3]), "Test case 3 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    run_tests()