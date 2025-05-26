from typing import List

class Solution:
    """
    LeetCode 735: Asteroid Collision

    Given a list of asteroids in a row, for each asteroid, the absolute value represents its size,
    and the sign represents its direction (positive = right, negative = left).
    Asteroids moving in the same direction never meet, but if two asteroids meet, the smaller one explodes.
    If they are the same size, both explode.

    The solution uses a stack to simulate the collisions.
    """

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            while stack and ast < 0 < stack[-1]:
                if stack[-1] < -ast:
                    stack.pop()
                    continue
                elif stack[-1] == -ast:
                    stack.pop()
                break
            else:
                stack.append(ast)
        return stack