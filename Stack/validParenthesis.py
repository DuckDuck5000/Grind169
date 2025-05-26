class Solution:
    def isValid(self, s: str) -> bool:
        hM = {
            "}":"{",
            "]":"[",
            ")":"("
        }
        stack = []
        for let in s:
            if let in hM:
                if not stack: return False
                if stack.pop() != hM[let]: return False
            else:
                stack.append(let)
        return len(stack) == 0