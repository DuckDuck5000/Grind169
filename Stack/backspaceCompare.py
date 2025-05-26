class Solution:
    """
    LeetCode 844: Backspace String Compare

    Given two strings s and t, return true if they are equal when both are typed into empty text editors.
    '#' means a backspace character.

    The solution uses stacks to simulate the typing process for both strings.
    """

    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(string):
            stack = []
            for char in string:
                if char == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(char)
            return stack

        return build(s) == build(t)