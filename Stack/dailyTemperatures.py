from typing import List

class Solution:
    """
    LeetCode 739: Daily Temperatures

    Given a list of daily temperatures, return a list such that, for each day,
    tells you how many days you would have to wait until a warmer temperature.
    If there is no future day for which this is possible, put 0 instead.

    The solution uses a monotonic decreasing stack to keep track of indices of unresolved temperatures.
    """

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []  # stores indices

        for i, temp in enumerate(temperatures):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                answer[prev_index] = i - prev_index
            stack.append(i)
        return answer