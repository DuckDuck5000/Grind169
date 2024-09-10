class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def helper(root):
            if root:
                temp = root.left
                root.left = root.right
                root.right = temp
                helper(root.right)
                helper(root.left)
                return root
        return helper(root)