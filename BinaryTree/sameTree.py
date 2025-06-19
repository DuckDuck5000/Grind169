"""
Same Tree

Problem Description:
------------------
Given the roots of two binary trees p and q, check if they are the same tree.
Two binary trees are considered the same if they are structurally identical 
and have the same node values.

Examples:
--------
Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false

Approach:
--------
1. Use recursive DFS to compare trees
2. Check if current nodes are equal
3. Recursively check left and right subtrees
4. Time Complexity: O(min(n,m)) where n,m are sizes of trees
5. Space Complexity: O(min(h1,h2)) where h1,h2 are heights
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both nodes are None, trees are same
        if not p and not q:
            return True
            
        # If one node is None, trees are different
        if not p or not q:
            return False
            
        # Check current nodes and recursively check subtrees
        return (p.val == q.val and 
                self.isSameTree(p.left, q.left) and 
                self.isSameTree(p.right, q.right))

def run_tests():
    """Test cases with assertions"""
    solution = Solution()
    
    # Test case 1: Identical trees
    p1 = TreeNode(1)
    p1.left = TreeNode(2)
    p1.right = TreeNode(3)
    
    q1 = TreeNode(1)
    q1.left = TreeNode(2)
    q1.right = TreeNode(3)
    
    assert solution.isSameTree(p1, q1) == True, "Test case 1 failed"
    
    # Test case 2: Different structure
    p2 = TreeNode(1)
    p2.left = TreeNode(2)
    
    q2 = TreeNode(1)
    q2.right = TreeNode(2)
    
    assert solution.isSameTree(p2, q2) == False, "Test case 2 failed"
    
    # Test case 3: Different values
    p3 = TreeNode(1)
    p3.left = TreeNode(2)
    p3.right = TreeNode(1)
    
    q3 = TreeNode(1)
    q3.left = TreeNode(1)
    q3.right = TreeNode(2)
    
    assert solution.isSameTree(p3, q3) == False, "Test case 3 failed"
    
    # Test case 4: Empty trees
    assert solution.isSameTree(None, None) == True, "Test case 4 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    run_tests()