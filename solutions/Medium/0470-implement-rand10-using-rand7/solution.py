# ──────────────────────────────────────────────────
# Problem  : 470. Implement Rand10() Using Rand7()
# Difficulty: Medium
# Tags     : Math, Rejection Sampling, Randomized, Probability and Statistics
# Link     : https://leetcode.com/problems/implement-rand10-using-rand7/
# Runtime  : 142 ms (beats 76%)
# Memory   : 21560000 (beats 47%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def rand10(self):
        curr = 40

        while curr >= 40:
            a, b = rand7(), rand7()
            curr = (a - 1) * 7 + (b - 1)

        return curr % 10 + 1