class Solution:
    """
    LeetCode 3: Longest Substring Without Repeating Characters
    
    Given a string s, find the length of the longest substring without repeating characters.
    Uses sliding window technique with a hash map to track character positions.
    """
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}  # Keep track of the most recent index of each char
        start = 0       # Start of current window
        max_length = 0  # Length of longest substring found
        
        for i, char in enumerate(s):
            # If we find a repeating character, move start pointer
            # to position after the last occurrence
            if char in char_index and char_index[char] >= start:
                start = char_index[char] + 1
            else:
                max_length = max(max_length, i - start + 1)
                
            char_index[char] = i
            
        return max_length
def test_longest_substring():
    solution = Solution()
    
    # Test cases
    assert solution.lengthOfLongestSubstring("abcabcbb") == 3  # "abc"
    assert solution.lengthOfLongestSubstring("bbbbb") == 1     # "b"
    assert solution.lengthOfLongestSubstring("pwwkew") == 3    # "wke"
    
    print("All test cases passed!")