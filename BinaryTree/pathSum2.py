"""
Path Sum II

Problem Description:
------------------
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths 
where the sum of the node values in the path equals targetSum. Each path should be 
returned as a list of node values.

Examples:
--------
Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22

Example 2:
Input: root = [1,2,3], targetSum = 5
Output: []

Approach:
--------
1. Use DFS with backtracking to track paths
2. Maintain current path and remaining sum
3. Add path to result when leaf node is reached and sum matches
4. Time Complexity: O(N²) where N is number of nodes
5. Space Complexity: O(H) where H is height of tree
"""

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node: TreeNode, remaining: int, path: List[int], result: List[List[int]]) -> None:
            if not node:
                return
            
            # Add current node to path
            path.append(node.val)
            
            # Check if we've reached a leaf node and sum matches
            if not node.left and not node.right and remaining == node.val:
                result.append(path[:])  # Add copy of path
                
            # Recurse on children
            dfs(node.left, remaining - node.val, path, result)
            dfs(node.right, remaining - node.val, path, result)
            
            # Backtrack
            path.pop()
        
        result = []
        dfs(root, targetSum, [], result)
        return result

def run_tests():
    """Test cases with assertions"""
    solution = Solution()
    
    # Test case 1: Multiple valid paths
    root1 = TreeNode(5)
    root1.left = TreeNode(4)
    root1.right = TreeNode(8)
    root1.left.left = TreeNode(11)
    root1.right.left = TreeNode(13)
    root1.right.right = TreeNode(4)
    root1.left.left.left = TreeNode(7)
    root1.left.left.right = TreeNode(2)
    root1.right.right.left = TreeNode(5)
    root1.right.right.right = TreeNode(1)
    
    result1 = solution.pathSum(root1, 22)
    expected1 = [[5,4,11,2], [5,8,4,5]]
    assert sorted(result1) == sorted(expected1), "Test case 1 failed"
    
    # Test case 2: No valid paths
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    assert solution.pathSum(root2, 5) == [], "Test case 2 failed"
    
    # Test case 3: Empty tree
    assert solution.pathSum(None, 0) == [], "Test case 3 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    run_tests()