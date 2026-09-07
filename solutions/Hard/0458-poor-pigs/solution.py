# ──────────────────────────────────────────────────
# Problem  : 458. Poor Pigs
# Difficulty: Hard
# Tags     : Math, Dynamic Programming, Combinatorics
# Link     : https://leetcode.com/problems/poor-pigs/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19280000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def poorPigs(self, buckets: int, timeDetect: int, timeTest: int) -> int:
        return ceil(log2(buckets)/log2(timeTest//timeDetect+1))
        