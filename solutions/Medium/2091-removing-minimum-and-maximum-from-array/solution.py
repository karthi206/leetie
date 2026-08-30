# ──────────────────────────────────────────────────
# Problem  : 2091. Removing Minimum and Maximum From Array
# Difficulty: Medium
# Tags     : Array, Greedy
# Link     : https://leetcode.com/problems/removing-minimum-and-maximum-from-array/
# Runtime  : 22 ms (beats 51%)
# Memory   : 33584000 (beats 63%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        minp, maxp, minel, maxel, L = 0, 0, float('inf'), float('-inf'), len(nums)
        for i, n in enumerate(nums):
            if n > maxel:
                maxel = n
                maxp = i
            if n < minel:
                minel = n
                minp = i
        
        left, right = min(minp, maxp), max(minp, maxp)

        return min(right + 1, L - left, left + 1 + (L - right))