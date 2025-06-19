"""
Construct Binary Tree from Preorder and Inorder Traversal

Problem Description:
------------------
Given two integer arrays preorder and inorder where preorder is the preorder traversal 
of a binary tree and inorder is the inorder traversal of the same tree, construct and 
return the binary tree.

Examples:
--------
Example 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Explanation: 
   3
  / \
 9  20
    /  \
   15   7

Example 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]

Approach:
--------
1. First element in preorder is always root
2. Find root in inorder to determine left and right subtrees
3. Recursively construct left and right subtrees
4. Use map for O(1) index lookups in inorder array
5. Time Complexity: O(n) where n is number of nodes
6. Space Complexity: O(n) for storing the map and recursion stack
"""

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Create index map for inorder traversal
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        def helper(pre_start: int, pre_end: int, in_start: int, in_end: int) -> Optional[TreeNode]:
            if pre_start > pre_end:
                return None
            
            # Root is first element in preorder
            root_val = preorder[pre_start]
            root = TreeNode(root_val)
            
            # Find root position in inorder
            root_idx = inorder_map[root_val]
            left_size = root_idx - in_start
            
            # Recursively build left and right subtrees
            root.left = helper(pre_start + 1, pre_start + left_size,
                             in_start, root_idx - 1)
            root.right = helper(pre_start + left_size + 1, pre_end,
                              root_idx + 1, in_end)
            
            return root
        
        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)

def run_tests():
    """Test cases with assertions"""
    solution = Solution()
    
    def compare_trees(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        return (root1.val == root2.val and
                compare_trees(root1.left, root2.left) and
                compare_trees(root1.right, root2.right))
    
    # Test case 1: Regular tree
    preorder1 = [3,9,20,15,7]
    inorder1 = [9,3,15,20,7]
    expected1 = TreeNode(3)
    expected1.left = TreeNode(9)
    expected1.right = TreeNode(20)
    expected1.right.left = TreeNode(15)
    expected1.right.right = TreeNode(7)
    result1 = solution.buildTree(preorder1, inorder1)
    assert compare_trees(result1, expected1), "Test case 1 failed"
    
    # Test case 2: Single node
    preorder2 = [-1]
    inorder2 = [-1]
    expected2 = TreeNode(-1)
    result2 = solution.buildTree(preorder2, inorder2)
    assert compare_trees(result2, expected2), "Test case 2 failed"
    
    # Test case 3: Empty tree
    preorder3 = []
    inorder3 = []
    assert solution.buildTree(preorder3, inorder3) is None, "Test case 3 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    run_tests()