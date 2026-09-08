# ──────────────────────────────────────────────────
# Problem  : 477. Total Hamming Distance
# Difficulty: Medium
# Tags     : Array, Math, Bit Manipulation
# Link     : https://leetcode.com/problems/total-hamming-distance/
# Runtime  : 142 ms (beats 75%)
# Memory   : 20752000 (beats 35%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            zero = one = 0
            mask = 1 << i
            for num in nums:
                if mask & num: one += 1
                else: zero += 1    
            ans += one * zero        
        return ans    