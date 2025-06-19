class Solution:
    """
    LeetCode 32: Longest Valid Parentheses
    
    Given a string containing just '(' and ')', find the length of the longest
    valid (well-formed) parentheses substring.
    
    The solution uses a stack to keep track of indices of unmatched parentheses.
    """
    
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # Initialize with -1 as base index
        max_length = 0
        
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:  # s[i] == ')'
                stack.pop()
                if not stack:
                    # No matching '(' found, mark new base
                    stack.append(i)
                else:
                    # Calculate length of valid substring
                    curr_length = i - stack[-1]
                    max_length = max(max_length, curr_length)
        
        return max_length