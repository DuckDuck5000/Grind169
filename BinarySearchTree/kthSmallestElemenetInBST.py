class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ## using inorder traversal helps a lot! cheater way tho

        count = 0
        ans = 0
        
        def inorder(root, k):
            nonlocal count, ans  # Declare nonlocal to modify outer variables
            if not root:
                return
            inorder(root.left, k)
            count += 1
            if k == count:
                ans = root.val
                return
            inorder(root.right, k)
        
        inorder(root, k)
        return ans
