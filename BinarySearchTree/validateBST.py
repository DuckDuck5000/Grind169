class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def helper(root, low, high):
            # Empty trees are valid BSTs.
            
            if root:
                if root.val <= low or root.val >= high:
                    return False
                right = helper(root.right, root.val, high)
                left = helper(root.left, low, root.val)
                return left and right
            return True
                    
        return helper(root, -math.inf, math.inf)