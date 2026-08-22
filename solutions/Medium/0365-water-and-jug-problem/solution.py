# ──────────────────────────────────────────────────
# Problem  : 365. Water and Jug Problem
# Difficulty: Medium
# Tags     : Math, Depth-First Search, Breadth-First Search, Bézout's Lemma, Euclidean Algorithm, Greatest Common Divisor, Extended Euclidean Algorithm
# Link     : https://leetcode.com/problems/water-and-jug-problem/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19564000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import deque

class Solution:
    def canMeasureWater(self, x, y, target):
        if target > x + y:
            return False

        stack = [(0, 0)]
        visited = set()

        while stack:
            a, b = stack.pop()

            if a + b == target:
                return True

            if (a, b) in visited:
                continue
            visited.add((a, b))

            stack.extend([(x, b), (a, y), (0, b), (a, 0)])

            w = min(a, y - b)
            stack.append((a - w, b + w))

            w = min(b, x - a)
            stack.append((a + w, b - w))

        return False