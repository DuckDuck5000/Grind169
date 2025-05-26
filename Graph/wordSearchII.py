from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    """
    LeetCode 212: Word Search II

    Given a 2D board and a list of words, find all words in the board.
    Each word must be constructed from letters of sequentially adjacent cells,
    where "adjacent" cells are horizontally or vertically neighboring.
    The same letter cell may not be used more than once in a word.

    We use a Trie to store the words and DFS to search the board efficiently.
    """

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Build Trie
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word

        rows, cols = len(board), len(board[0])
        result = set()

        def dfs(r, c, node):
            if (r < 0 or r >= rows or c < 0 or c >= cols or
                board[r][c] not in node.children):
                return
            char = board[r][c]
            next_node = node.children[char]
            if next_node.word:
                result.add(next_node.word)
                next_node.word = None  # Avoid duplicates

            board[r][c] = '#'  # Mark as visited
            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                dfs(r + dr, c + dc, next_node)
            board[r][c] = char  # Restore

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return list(result)