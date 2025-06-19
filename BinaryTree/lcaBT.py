"""
Lowest Common Ancestor of a Binary Tree

Problem Description:
------------------
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
The lowest common ancestor is defined between two nodes p and q as the lowest node in T 
that has both p and q as descendants.

Examples:
--------
Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself.

Approach:
--------
1. Use recursive DFS to search for nodes p and q
2. If current node is p or q, return it
3. Search left and right subtrees
4. If both subtrees return non-null, current node is LCA
5. Time Complexity: O(n) where n is number of nodes
6. Space Complexity: O(h) where h is height of tree
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base case: if root is None or equals p or q
        if not root or root == p or root == q:
            return root
            
        # Search in left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # If both left and right are non-null, root is LCA
        if left and right:
            return root
            
        # Return non-null node
        return left if left else right

def run_tests():
    """Test cases with assertions"""
    solution = Solution()
    
    # Test case 1: Regular case
    root1 = TreeNode(3)
    root1.left = TreeNode(5)
    root1.right = TreeNode(1)
    root1.left.left = TreeNode(6)
    root1.left.right = TreeNode(2)
    root1.right.left = TreeNode(0)
    root1.right.right = TreeNode(8)
    root1.left.right.left = TreeNode(7)
    root1.left.right.right = TreeNode(4)
    
    # LCA of 5 and 1 should be 3
    assert solution.lowestCommonAncestor(root1, root1.left, root1.right).val == 3, "Test case 1 failed"
    
    # Test case 2: Node is ancestor of itself
    # LCA of 5 and 4 should be 5
    assert solution.lowestCommonAncestor(root1, root1.left, root1.left.right.right).val == 5, "Test case 2 failed"
    
    # Test case 3: Nodes in same subtree
    # LCA of 6 and 7 should be 5
    assert solution.lowestCommonAncestor(root1, root1.left.left, root1.left.right.left).val == 5, "Test case 3 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    run_tests()