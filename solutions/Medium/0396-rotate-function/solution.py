# ──────────────────────────────────────────────────
# Problem  : 396. Rotate Function
# Difficulty: Medium
# Tags     : Array, Math, Dynamic Programming
# Link     : https://leetcode.com/problems/rotate-function/
# Runtime  : 158 ms (beats 18%)
# Memory   : 31292000 (beats 30%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        a_sum = 0
        F = 0
        n = len(A)

        for i in range(n):
            a_sum += A[i]
            F += i * A[i]

        res = F

        for i in range(1, n):
            F += a_sum - n * A[-i]
            res = max(res, F)

        return res