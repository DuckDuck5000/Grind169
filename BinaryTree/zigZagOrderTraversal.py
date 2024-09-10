class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        output = []
        if not root: return output
        q = [root]
        flip = False

        while q:
            temp = []
            n = len(q)
            for _ in range(n):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                temp.append(node.val)
            if flip:
                output.append(temp[::-1])
            else:
                output.append(temp)
            flip = not flip
        return output