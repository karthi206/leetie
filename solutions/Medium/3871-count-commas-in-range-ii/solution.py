# ──────────────────────────────────────────────────
# Problem  : 3871. Count Commas in Range II
# Difficulty: Medium
# Tags     : Math
# Link     : https://leetcode.com/problems/count-commas-in-range-ii/
# Runtime  : 0 ms (beats 100%)
# Memory   : 19140000 (beats 88%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def countCommas(self, n: int) -> int:
        k = (len(str(n)) - 1) // 3 # int(log10(n)) // 3 
        return k * (n + 1) - (1000**(k + 1) - 1000) // 999