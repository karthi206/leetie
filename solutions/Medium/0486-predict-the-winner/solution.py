# ──────────────────────────────────────────────────
# Problem  : 486. Predict the Winner
# Difficulty: Medium
# Tags     : Array, Math, Dynamic Programming, Recursion, Minimax, Game Theory, Zero-Sum Game
# Link     : https://leetcode.com/problems/predict-the-winner/
# Runtime  : 3 ms (beats 45%)
# Memory   : 19812000 (beats 26%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def predictTheWinner(self, A: List[int]) -> bool:
        n = len(A)
        if ~n & 1: return True

        @cache
        def maxDiff(i: int, j: int) -> int:
            if i == j: return A[i]
            return max(A[i] - maxDiff(i + 1, j),
                       A[j] - maxDiff(i, j - 1))

        return maxDiff(0, n - 1) >= 0