# ──────────────────────────────────────────────────
# Problem  : 137. Single Number II
# Difficulty: Medium
# Tags     : Array, Bit Manipulation
# Link     : https://leetcode.com/problems/single-number-ii/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19340000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result=0
        for i in range(32):
            bit_sum=0
            for num in nums:
                bit_sum+=(num>>i)&1
            if bit_sum %3 !=0:
                result |=(1<<i)
        if result>= (1<<31):
            result-=(1<<32)
        return result 