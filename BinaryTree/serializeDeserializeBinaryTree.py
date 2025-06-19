"""
Serialize and Deserialize Binary Tree

Problem Description:
------------------
Design an algorithm to serialize and deserialize a binary tree. The encoded string should
be as compact as possible. You need to design an algorithm to serialize a binary tree into
a string and deserialize the string back to the original tree structure.

Examples:
--------
Example 1:
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
Explanation: 
   1
  / \
 2   3
    / \
   4   5

Example 2:
Input: root = []
Output: []

Approach:
--------
1. Use preorder traversal for serialization
2. Use string tokens with delimiter for serialization
3. Use queue for deserialization
4. Use "null" to mark empty nodes
5. Time Complexity: O(n) for both operations
6. Space Complexity: O(n) for string representation
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string."""
        if not root:
            return "null"
        
        return (str(root.val) + "," + 
                self.serialize(root.left) + "," + 
                self.serialize(root.right))

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree."""
        def dfs() -> TreeNode:
            val = next(values)
            if val == "null":
                return None
                
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node
        
        values = iter(data.split(","))
        return dfs()

def run_tests():
    """Test cases with assertions"""
    codec = Codec()
    
    # Test case 1: Regular binary tree
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.right.left = TreeNode(4)
    root1.right.right = TreeNode(5)
    
    serialized1 = codec.serialize(root1)
    deserialized1 = codec.deserialize(serialized1)
    
    # Helper function to compare trees
    def is_same_tree(p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return (p.val == q.val and 
                is_same_tree(p.left, q.left) and 
                is_same_tree(p.right, q.right))
    
    assert is_same_tree(root1, deserialized1), "Test case 1 failed"
    
    # Test case 2: Empty tree
    assert codec.deserialize(codec.serialize(None)) is None, "Test case 2 failed"
    
    # Test case 3: Single node tree
    root3 = TreeNode(1)
    serialized3 = codec.serialize(root3)
    deserialized3 = codec.deserialize(serialized3)
    assert is_same_tree(root3, deserialized3), "Test case 3 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    run_tests()