from typing import List
from collections import deque, defaultdict

class Solution:
    """
    LeetCode 815: Bus Routes

    You are given a list of bus routes where routes[i] is a list of bus stops that the i-th bus repeats forever.
    Given a source and target bus stop, return the minimum number of buses you must take to travel from source to target.
    If it is not possible, return -1.

    This is a graph problem where each bus stop is a node, and you can move between stops on the same bus route.
    BFS is used to find the shortest path (minimum buses) from source to target.
    """

    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        # Map each stop to the list of buses (routes) that visit it
        stop_to_buses = defaultdict(set)
        for bus, stops in enumerate(routes):
            for stop in stops:
                stop_to_buses[stop].add(bus)

        visited_stops = set()
        visited_buses = set()
        queue = deque([(source, 0)])  # (current stop, buses taken)

        while queue:
            stop, buses_taken = queue.popleft()
            if stop == target:
                return buses_taken
            for bus in stop_to_buses[stop]:
                if bus in visited_buses:
                    continue
                visited_buses.add(bus)
                for next_stop in routes[bus]:
                    if next_stop not in visited_stops:
                        visited_stops.add(next_stop)
                        queue.append((next_stop, buses_taken + 1))
        return -1