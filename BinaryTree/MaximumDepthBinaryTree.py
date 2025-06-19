"""
Maximum Depth of Binary Tree (Iterative DFS Approach)

Problem Description:
------------------
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path 
from the root node down to the farthest leaf node.

Examples:
--------
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3
Explanation: Depth is 3 (path: 3->20->7 or 3->20->15)

Example 2:
Input: root = [1,null,2]
Output: 2

Approach:
--------
1. Use iterative DFS with a helper function
2. Track current depth during traversal
3. Update maximum depth seen so far
4. Time Complexity: O(n) where n is number of nodes
5. Space Complexity: O(h) where h is height of tree
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:        
        self.maxDepth = 0
        def helper(tempDepth, root):
            if root:
                tempDepth += 1
                self.maxDepth = max(self.maxDepth, tempDepth)
                helper(tempDepth, root.left)
                helper(tempDepth, root.right)
        helper(0, root)
        return self.maxDepth

def run_tests():
    """Test cases with assertions"""
    solution = Solution()
    
    # Test case 1: Regular balanced tree
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    assert solution.maxDepth(root1) == 3, "Test case 1 failed"
    
    # Test case 2: Single node
    root2 = TreeNode(1)
    assert solution.maxDepth(root2) == 1, "Test case 2 failed"
    
    # Test case 3: Empty tree
    assert solution.maxDepth(None) == 0, "Test case 3 failed"
    
    # Test case 4: Unbalanced tree
    root4 = TreeNode(1)
    root4.left = TreeNode(2)
    root4.left.left = TreeNode(3)
    root4.left.left.left = TreeNode(4)
    assert solution.maxDepth(root4) == 4, "Test case 4 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    run_tests()