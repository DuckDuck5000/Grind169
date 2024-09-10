class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        if root is None:
            return 0
        
        lheight= self.height(root.left)
        rheight = self.height(root.right)
        
        ldiameter = self.diameterOfBinaryTree(root.left)
        rdiameter = self.diameterOfBinaryTree(root.right)
        
        return max(lheight + rheight, max(ldiameter,rdiameter))
    
    def height(self, node):
        if node is None:
            return 0
        
        return 1 + max(self.height(node.left), self.height(node.right))