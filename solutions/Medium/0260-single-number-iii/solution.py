# ──────────────────────────────────────────────────
# Problem  : 260. Single Number III
# Difficulty: Medium
# Tags     : Array, Bit Manipulation
# Link     : https://leetcode.com/problems/single-number-iii/
# Runtime  : 6 ms (beats 20%)
# Memory   : 20968000 (beats 43%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0

        for num in nums:
            xor ^= num

        diff = xor & -xor

        a = 0
        b = 0

        for num in nums:
            if num & diff:
                a ^= num
            else:
                b ^= num

        return [a, b]