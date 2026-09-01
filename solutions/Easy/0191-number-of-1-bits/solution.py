# ──────────────────────────────────────────────────
# Problem  : 191. Number of 1 Bits
# Difficulty: Easy
# Tags     : Divide and Conquer, Bit Manipulation
# Link     : https://leetcode.com/problems/number-of-1-bits/
# Runtime  : 0 ms (beats 100%)
# Memory   : 19344000 (beats 23%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        while n:
            n=n&(n-1)
            count+=1
        return count