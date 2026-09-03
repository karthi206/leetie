# ──────────────────────────────────────────────────
# Problem  : 343. Integer Break
# Difficulty: Medium
# Tags     : Math, Dynamic Programming
# Link     : https://leetcode.com/problems/integer-break/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19276000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2

        # Try to divide n into as many threes as possible
        threes = n // 3
        remainder = n % 3

        if remainder == 1:
            threes -= 1 # remove 3 * 1
            remainder = 4 # create 2 * 2
        elif remainder == 0:
            remainder = 1 # when remainder is 0, set 1 which doesn't affect your answer.

        return (3 ** threes) * remainder