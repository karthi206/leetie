# ──────────────────────────────────────────────────
# Problem  : 310. Minimum Height Trees
# Difficulty: Medium
# Tags     : Depth-First Search, Breadth-First Search, Graph Theory, Topological Sort
# Link     : https://leetcode.com/problems/minimum-height-trees/
# Runtime  : 47 ms (beats 63%)
# Memory   : 27872000 (beats 70%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import defaultdict, deque
from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        # Edge case: single node
        if n == 1:
            return [0]

        # Adjacency list
        adj = defaultdict(list)
        degree = [0] * n

        # Build graph
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            degree[u] += 1
            degree[v] += 1

        # Queue of leaf nodes
        q = deque()

        # Push initial leaf nodes
        for i in range(n):
            if degree[i] == 1:
                q.append(i)

        nodes = n

        # Trim leaves layer by layer
        while nodes > 2:
            size = len(q)
            nodes -= size

            for _ in range(size):
                curr = q.popleft()

                for nei in adj[curr]:
                    degree[nei] -= 1

                    # If it becomes a leaf
                    if degree[nei] == 1:
                        q.append(nei)

        # Remaining nodes are MHT roots
        return list(q)