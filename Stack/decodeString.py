class Solution:
    """
    LeetCode 394: Decode String

    Given an encoded string, return its decoded string.
    The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is repeated exactly k times.

    The solution uses a stack to keep track of numbers and previous strings.
    """

    def decodeString(self, s: str) -> str:
        stack = []
        curr_num = 0
        curr_str = ""

        for char in s:
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)
            elif char == "[":
                stack.append((curr_str, curr_num))
                curr_str = ""
                curr_num = 0
            elif char == "]":
                prev_str, num = stack.pop()
                curr_str = prev_str + num * curr_str
            else:
                curr_str += char

        return curr_str