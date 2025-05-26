from typing import List
from collections import defaultdict, deque

class Solution:
    """
    LeetCode 210: Course Schedule II

    Given the total number of courses and a list of prerequisite pairs,
    return a possible order to finish all courses (topological sort).
    If it is not possible to finish all courses, return an empty list.
    """

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Build the adjacency list and in-degree array
        adj = defaultdict(list)
        in_degree = [0] * numCourses

        for dest, src in prerequisites:
            adj[src].append(dest)
            in_degree[dest] += 1

        # Queue for courses with no prerequisites
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        order = []

        while queue:
            course = queue.popleft()
            order.append(course)
            for neighbor in adj[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # If all courses are in the order, return it; otherwise, return []
        return order if len(order) == numCourses else []