class Solution:
    """
    LeetCode 224: Basic Calculator
    
    Given a string s representing a valid expression, implement a basic calculator to evaluate it.
    The expression string may contain '(', ')', '+', '-', non-negative integers and spaces.
    
    Handles parentheses using a stack
    No multiplication or division to worry about
    Only needs to deal with addition and subtraction
    Keeps track of signs separately
    
    """
    
    def calculate(self, s: str) -> int:
        stack = []
        result = 0 
        number = 0 
        sign = 1   
        
        for char in s:
            if char.isdigit():
                number = number * 10 + int(char)
            elif char == '+':
                result += sign * number
                number = 0
                sign = 1
            elif char == '-':
                result += sign * number
                number = 0
                sign = -1
            elif char == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif char == ')':
                result += sign * number
                number = 0
                result *= stack.pop()
                result += stack.pop()
                
        return result + (sign * number)