# ──────────────────────────────────────────────────
# Problem  : 375. Guess Number Higher or Lower II
# Difficulty: Medium
# Tags     : Math, Dynamic Programming, Minimax, Game Theory
# Link     : https://leetcode.com/problems/guess-number-higher-or-lower-ii/
# Runtime  : 3616 ms (beats 5%)
# Memory   : 21748000 (beats 43%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        def dp(i, j, memo: dict):
            if i >= j:
                return 0
            if (i, j) not in memo:
                memo[(i, j)] = float('inf')
                for x in range(i, j+1):
                    lower = dp(i, x-1, memo)
                    higher = dp(x+1, j, memo)
                    memo[(i, j)] = min(memo[(i, j)], x + max(lower, higher))
            return memo[(i, j)]
        return dp(1, n, {})