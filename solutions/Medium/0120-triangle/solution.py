# ──────────────────────────────────────────────────
# Problem  : 120. Triangle
# Difficulty: Medium
# Tags     : Array, Dynamic Programming
# Link     : https://leetcode.com/problems/triangle/
# Runtime  : 1 ms (beats 81%)
# Memory   : 20132000 (beats 46%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def minimumTotal(self, tri: List[List[int]]) -> int:
        for i in range(len(tri) - 2, -1, -1):
            for j in range(len(tri[i])):
                tri[i][j] += min(tri[i + 1][j], tri[i + 1][j + 1])
        return tri[0][0]