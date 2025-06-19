"""
Binary Tree Maximum Path Sum

Problem Description:
------------------
Given the root of a binary tree, return the maximum path sum of any non-empty path.
A path is defined as any sequence of nodes from some starting node to any node in the 
tree along the parent-child connections. The path must contain at least one node and 
does not need to go through the root.

Examples:
--------
Example 1:
Input: root = [1,2,3]
Output: 6
Explanation: Optimal path is 2 -> 1 -> 3 with path sum = 6

Example 2:
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: Optimal path is 15 -> 20 -> 7 with path sum = 42

Approach:
--------
1. Use recursive DFS with a global max variable
2. At each node, calculate max path through current node
3. Update global max if current path is larger
4. Return max path that can be extended by parent
5. Time Complexity: O(n) where n is number of nodes
6. Space Complexity: O(h) where h is height of tree
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def max_gain(node: TreeNode) -> int:
            if not node:
                return 0
            
            # Get max path sum from left and right subtrees
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            
            # Update max_sum if path through current node is larger
            path_sum = node.val + left_gain + right_gain
            self.max_sum = max(self.max_sum, path_sum)
            
            # Return maximum path that can be extended by parent
            return node.val + max(left_gain, right_gain)
        
        self.max_sum = float('-inf')
        max_gain(root)
        return self.max_sum

def run_tests():
    """Test cases with assertions"""
    solution = Solution()
    
    # Test case 1: Simple tree with positive values
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    assert solution.maxPathSum(root1) == 6, "Test case 1 failed"
    
    # Test case 2: Tree with negative values
    root2 = TreeNode(-10)
    root2.left = TreeNode(9)
    root2.right = TreeNode(20)
    root2.right.left = TreeNode(15)
    root2.right.right = TreeNode(7)
    assert solution.maxPathSum(root2) == 42, "Test case 2 failed"
    
    # Test case 3: Single node
    root3 = TreeNode(-3)
    assert solution.maxPathSum(root3) == -3, "Test case 3 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    run_tests()