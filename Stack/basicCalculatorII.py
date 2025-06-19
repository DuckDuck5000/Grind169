class Solution:
    """
    LeetCode 227: Basic Calculator II
    
    Given a string s which represents an expression, evaluate this expression and return its value.
    The integer division should truncate toward zero.
    You may assume that the given expression is always valid.
    
    Example:
    Input: s = "3+2*2"
    Output: 7
    """
    
    def calculate(self, s: str) -> int:
        stack = []
        curr_num = 0
        operation = '+'
        
        for i, char in enumerate(s):
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)
                
            if (not char.isdigit() and char != ' ') or i == len(s) - 1:
                if operation == '+':
                    stack.append(curr_num)
                elif operation == '-':
                    stack.append(-curr_num)
                elif operation == '*':
                    stack.append(stack.pop() * curr_num)
                elif operation == '/':
                    # Handle division by rounding towards 0
                    prev = stack.pop()
                    if prev < 0:
                        stack.append(-((-prev) // curr_num))
                    else:
                        stack.append(prev // curr_num)
                
                operation = char
                curr_num = 0
                
        return sum(stack)