"""
Symmetric Tree

Problem Description:
------------------
Given the root of a binary tree, check whether it is a mirror of itself 
(i.e., symmetric around its center).

Examples:
--------
Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true
Explanation: The tree is symmetric around its center

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false
Explanation: The tree is not symmetric

Approach:
--------
1. Use recursive approach comparing left and right subtrees
2. Check if values are equal and subtrees are mirror images
3. A tree is symmetric if:
   - Root's left and right subtrees are mirror images
   - For each node pair: values equal and their subtrees are mirrors
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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            # If both nodes are None, they're symmetric
            if not left and not right:
                return True
            
            # If one node is None, not symmetric
            if not left or not right:
                return False
            
            # Check current values and recursive check subtrees
            return (left.val == right.val and
                    isMirror(left.left, right.right) and
                    isMirror(left.right, right.left))
        
        if not root:
            return True
        return isMirror(root.left, root.right)

def run_tests():
    """Test cases with assertions"""
    solution = Solution()
    
    # Test case 1: Symmetric tree
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(2)
    root1.left.left = TreeNode(3)
    root1.left.right = TreeNode(4)
    root1.right.left = TreeNode(4)
    root1.right.right = TreeNode(3)
    assert solution.isSymmetric(root1) == True, "Test case 1 failed"
    
    # Test case 2: Non-symmetric tree
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(2)
    root2.left.right = TreeNode(3)
    root2.right.right = TreeNode(3)
    assert solution.isSymmetric(root2) == False, "Test case 2 failed"
    
    # Test case 3: Empty tree
    assert solution.isSymmetric(None) == True, "Test case 3 failed"
    
    # Test case 4: Single node
    root4 = TreeNode(1)
    assert solution.isSymmetric(root4) == True, "Test case 4 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    run_tests()