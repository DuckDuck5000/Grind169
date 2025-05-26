from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    LeetCode 235: Lowest Common Ancestor of a Binary Search Tree

    Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
    The LCA is defined as the lowest node in the tree that has both nodes as descendants (a node can be a descendant of itself).

    Because it's a BST, for any node:
      - All values in the left subtree are less than the node's value.
      - All values in the right subtree are greater than the node's value.
    """

    def lowestCommonAncestor(self, root: Optional[TreeNode], p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
        # Traverse the tree starting from root
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left  # Both nodes are in the left subtree
            elif p.val > root.val and q.val > root.val:
                root = root.right  # Both nodes are in the right subtree
            else:
                return root  # This is the split point, so root is LCA
        return None