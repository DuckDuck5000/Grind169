"""
Word Break (Trie Solution)

Problem Description:
------------------
Given a string s and a dictionary of strings wordDict, return true if s can be 
segmented into a space-separated sequence of one or more dictionary words.

Approach using Trie:
------------------
1. Build a trie from the dictionary words
2. Use DFS with memoization to check string segments
3. At each position, traverse trie and string simultaneously
4. Time Complexity: O(n * m) where n is length of s, m is max word length
5. Space Complexity: O(k) where k is total characters in dictionary
"""

from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Solution:
    def buildTrie(self, wordDict: List[str]) -> TrieNode:
        root = TrieNode()
        for word in wordDict:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_word = True
        return root
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root = self.buildTrie(wordDict)
        n = len(s)
        memo = {}
        
        def dfs(start: int) -> bool:
            if start == n:
                return True
            if start in memo:
                return memo[start]
            
            node = root
            for i in range(start, n):
                if s[i] not in node.children:
                    break
                node = node.children[s[i]]
                if node.is_word and dfs(i + 1):
                    memo[start] = True
                    return True
            
            memo[start] = False
            return False
        
        return dfs(0)

def run_tests():
    """Test cases with assertions"""
    solution = Solution()
    
    # Test case 1: Basic case
    s1 = "leetcode"
    wordDict1 = ["leet", "code"]
    assert solution.wordBreak(s1, wordDict1) == True, "Test case 1 failed"
    
    # Test case 2: Repeated words
    s2 = "applepenapple"
    wordDict2 = ["apple", "pen"]
    assert solution.wordBreak(s2, wordDict2) == True, "Test case 2 failed"
    
    # Test case 3: Cannot be segmented
    s3 = "catsandog"
    wordDict3 = ["cats", "dog", "sand", "and", "cat"]
    assert solution.wordBreak(s3, wordDict3) == False, "Test case 3 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    run_tests()