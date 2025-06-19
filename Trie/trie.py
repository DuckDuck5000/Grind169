"""
Implement Trie (Prefix Tree)

Problem Description:
------------------
Implement a trie with insert, search, and startsWith methods.
- Trie() Initializes the trie object
- insert(word) Inserts the string word into the trie
- search(word) Returns true if word is in the trie (i.e., was inserted), false otherwise
- startsWith(prefix) Returns true if there is any word in the trie that starts with prefix

Examples:
--------
Input:
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output:
[null, null, true, false, true, null, true]

Explanation:
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True

Approach:
--------
1. Use TrieNode class with children map and word flag
2. Insert: Add characters one by one, mark last node as word
3. Search: Navigate to last character, check if it's a word
4. StartsWith: Navigate to last character of prefix
5. Time Complexity: O(m) for all operations where m is key length
6. Space Complexity: O(N) where N is total characters in trie
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

def run_tests():
    """Test cases with assertions"""
    trie = Trie()
    
    # Test case 1: Basic operations
    trie.insert("apple")
    assert trie.search("apple"), "Test case 1.1 failed"
    assert not trie.search("app"), "Test case 1.2 failed"
    assert trie.startsWith("app"), "Test case 1.3 failed"
    
    # Test case 2: Insert shorter word
    trie.insert("app")
    assert trie.search("app"), "Test case 2 failed"
    
    # Test case 3: Non-existent words
    assert not trie.search("appl"), "Test case 3.1 failed"
    assert not trie.search("aptitude"), "Test case 3.2 failed"
    
    # Test case 4: Multiple words with common prefix
    trie.insert("aptitude")
    assert trie.startsWith("apt"), "Test case 4.1 failed"
    assert trie.search("aptitude"), "Test case 4.2 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    run_tests()