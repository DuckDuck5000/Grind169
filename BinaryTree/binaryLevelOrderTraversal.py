class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        output = []
        temp = []
        q = [root]

        while q:
          
            temp = []
            n = len(q)
            for _ in range(n):
                node = q.pop(0)
                temp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            output.append(temp)
        return output