# ──────────────────────────────────────────────────
# Problem  : 78. Subsets
# Difficulty: Medium
# Tags     : Array, Backtracking, Bit Manipulation
# Link     : https://leetcode.com/problems/subsets/
# Runtime  : 0 ms (beats 100%)
# Memory   : 19564000 (beats 5%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        result=[]
        for mask in range(1<<n):
            subset=[]
            for i in range(n):
                if (mask & (1<<i))!=0:
                    subset.append(nums[i])
            result.append(subset)
        return result
    