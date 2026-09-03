# ──────────────────────────────────────────────────
# Problem  : 371. Sum of Two Integers
# Difficulty: Medium
# Tags     : Math, Bit Manipulation
# Link     : https://leetcode.com/problems/sum-of-two-integers/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19084000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        
        
        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask
        
        
        return a if a < 0x80000000 else ~(a ^ mask)