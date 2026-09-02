# ──────────────────────────────────────────────────
# Problem  : 137. Single Number II
# Difficulty: Medium
# Tags     : Array, Bit Manipulation
# Link     : https://leetcode.com/problems/single-number-ii/
# Runtime  : 29 ms (beats 23%)
# Memory   : 20648000 (beats 47%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        
        for i in range(32):
            bit_sum = 0
            for num in nums:
                # Use (num >> i) & 1 to safely extract the i-th bit for negative inputs
                bit_sum += (num >> i) & 1
            
            if bit_sum % 3 != 0:
                result |= (1 << i)
        
        # Convert unsigned 32-bit integer back to 32-bit signed integer
        if result >= (1 << 31):
            result -= (1 << 32)
            
        return result