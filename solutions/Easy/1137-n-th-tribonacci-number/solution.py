# ──────────────────────────────────────────────────
# Problem  : 1137. N-th Tribonacci Number
# Difficulty: Easy
# Tags     : Math, Dynamic Programming, Memoization
# Link     : https://leetcode.com/problems/n-th-tribonacci-number/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19348000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from functools import lru_cache

class Solution:
    @lru_cache(maxsize=None)  # Keeps the recursion fast so LeetCode accepts it
    def tribonacci(self, n: int) -> int:
        # Base Cases
        if n == 0: 
            return 0
        if n == 1 or n == 2: 
            return 1
            
        # Recursive Case (fixed with self. and correct math)
        return self.tribonacci(n-3) + self.tribonacci(n-2) + self.tribonacci(n-1)
