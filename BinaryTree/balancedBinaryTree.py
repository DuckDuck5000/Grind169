class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        

        def checkHeight(root):
            if not root: return 0

            left = checkHeight(root.left)
            if left == -1: return -1
            right = checkHeight(root.right)
            if right == -1: return -1
            if abs(right-left) > 1: return -1
            return 1 + max(left, right)
        return checkHeight(root) != -1