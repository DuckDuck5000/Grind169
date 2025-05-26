from typing import List
from collections import defaultdict, deque

class Solution:
    """
    LeetCode 269: Alien Dictionary

    Given a list of words sorted lexicographically according to an unknown alien language,
    return a string of the unique letters in the correct order of the alien alphabet.
    If there is no valid order, return "".

    This is a graph problem where each letter is a node, and an edge from letter A to B
    means A comes before B. We use topological sorting to find a valid letter order.
    """

    def alienOrder(self, words: List[str]) -> str:
        # Build the graph
        adj = defaultdict(set)
        in_degree = {c: 0 for word in words for c in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            if w1[:min_len] == w2[:min_len] and len(w1) > len(w2):
                return ""  # Invalid order (prefix case)
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if c2 not in adj[c1]:
                        adj[c1].add(c2)
                        in_degree[c2] += 1
                    break

        # Topological sort (Kahn's algorithm)
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        order = []

        while queue:
            c = queue.popleft()
            order.append(c)
            for neighbor in adj[c]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return "".join(order) if len(order) == len(in_degree) else ""