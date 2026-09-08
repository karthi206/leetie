# ──────────────────────────────────────────────────
# Problem  : 3870. Count Commas in Range
# Difficulty: Easy
# Tags     : Math
# Link     : https://leetcode.com/problems/count-commas-in-range/
# Runtime  : 330 ms (beats 14%)
# Memory   : 19232000 (beats 47%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def countCommas(self, n: int) -> int:
        count = 0

        for i in range(1, n + 1):
            if i >= 1000:
                count += 1

        return count