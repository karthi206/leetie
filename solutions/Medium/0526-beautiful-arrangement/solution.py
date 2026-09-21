# ──────────────────────────────────────────────────
# Problem  : 526. Beautiful Arrangement
# Difficulty: Medium
# Tags     : Array, Dynamic Programming, Backtracking, Bit Manipulation, Bitmask
# Link     : https://leetcode.com/problems/beautiful-arrangement/
# Runtime  : 46 ms (beats 91%)
# Memory   : 24440000 (beats 8%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def countArrangement(self, n: int) -> int:
        # mask: what number from 1 to n is avaliable to use
        @cache
        def ways(i, mask):
            if i > n:
                return 1
            count = 0
            for p in range(1, n+1):
                if (mask & 1 << p) == 0 and (i % p == 0 or p % i == 0):
                    count += ways(i+1, mask | 1 << p)
            return count
        return ways(1, 0)