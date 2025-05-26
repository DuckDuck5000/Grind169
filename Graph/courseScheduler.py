from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # Build the adjacency list and in-degree array
        adj = defaultdict(list)
        in_degree = [0] * numCourses

        for dest, src in prerequisites:
            adj[src].append(dest)
            in_degree[dest] += 1

        # Use a list as a stack for nodes with in-degree 0
        stack = [i for i in range(numCourses) if in_degree[i] == 0]
        taken = 0

        while stack:
            course = stack.pop(0)  # Remove from front to simulate queue behavior
            taken += 1
            for neighbor in adj[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    stack.append(neighbor)

        return taken == numCourses