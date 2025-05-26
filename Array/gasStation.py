from typing import List

class Solution:
    """
    LeetCode 134: Gas Station

    There are n gas stations along a circular route, where the amount of gas at the i-th station is gas[i],
    and the cost to travel from station i to i+1 is cost[i].
    Return the starting gas station's index if you can travel around the circuit once in the clockwise direction,
    otherwise return -1.

    The solution checks if the total gas is at least the total cost, and finds the correct starting index using a greedy approach.
    """

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        total, start = 0, 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                start = i + 1
                total = 0
        return start