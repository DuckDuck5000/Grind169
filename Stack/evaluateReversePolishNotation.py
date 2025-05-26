from typing import List

class Solution:
    """
    LeetCode 150: Evaluate Reverse Polish Notation

    Evaluate the value of an arithmetic expression in Reverse Polish Notation (RPN).
    Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

    The solution uses a stack to process the tokens.
    """

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:  # token == "/"
                    # Truncate towards zero
                    stack.append(int(a / b))
            else:
                stack.append(int(token))
        return stack[0]