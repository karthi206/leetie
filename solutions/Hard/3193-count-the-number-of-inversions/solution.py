# ──────────────────────────────────────────────────
# Problem  : 3193. Count the Number of Inversions
# Difficulty: Hard
# Tags     : Array, Dynamic Programming
# Link     : https://leetcode.com/problems/count-the-number-of-inversions/
# Runtime  : 47 ms (beats 0%)
# Memory   : 19200000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
        return n-1