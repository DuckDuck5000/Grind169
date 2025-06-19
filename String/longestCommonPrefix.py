class Solution:
    """
    LeetCode 14: Longest Common Prefix
    
    Write a function to find the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string "".
    
    Example:
    Input: strs = ["flower","flow","flight"]
    Output: "fl"
    """
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Handle edge cases
        if not strs:
            return ""
            
        # Take first string as reference
        for i, char in enumerate(strs[0]):
            # Check this char against same position in all other strings
            for other in strs[1:]:
                # If we've reached the end of another string
                # or found a mismatch
                if i >= len(other) or other[i] != char:
                    return strs[0][:i]
        
        # If we get here, first string is the prefix
        return strs[0]