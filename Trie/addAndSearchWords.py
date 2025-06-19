"""
Design Add and Search Words Data Structure

Problem Description:
------------------
Design a data structure that supports adding new words and finding if a string matches
any previously added string. Word may contain dots '.' where dots can be matched with
any letter.

Examples:
--------
Input:
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output:
[null,null,null,null,false,true,true,true]

Explanation:
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True

Approach:
--------
1. Use Trie structure with wildcard search capability
2. For dots, try all possible characters at that position
3. Use DFS for wildcard search
4. Time Complexity: 
   - addWord: O(m) where m is word length
   - search: O(26^n) worst case for all dots
5. Space Complexity: O(N) where N is total characters in all words
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def search(self, word: str) -> bool:
        def dfs(node: TrieNode, i: int) -> bool:
            # Base case: reached end of word
            if i == len(word):
                return node.is_word
            
            # Current character is dot
            if word[i] == '.':
                # Try all possible characters
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False
            
            # Normal character
            if word[i] not in node.children:
                return False
            return dfs(node.children[word[i]], i + 1)
        
        return dfs(self.root, 0)

def run_tests():
    """Test cases with assertions"""
    wordDict = WordDictionary()
    
    # Test case 1: Basic word operations
    wordDict.addWord("bad")
    wordDict.addWord("dad")
    wordDict.addWord("mad")
    assert not wordDict.search("pad"), "Test case 1.1 failed"
    assert wordDict.search("bad"), "Test case 1.2 failed"
    
    # Test case 2: Dot pattern matching
    assert wordDict.search(".ad"), "Test case 2.1 failed"
    assert wordDict.search("b.."), "Test case 2.2 failed"
    assert not wordDict.search("b.x"), "Test case 2.3 failed"
    
    # Test case 3: Empty and edge cases
    assert not wordDict.search(""), "Test case 3.1 failed"
    assert not wordDict.search("...."), "Test case 3.2 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    run_tests()