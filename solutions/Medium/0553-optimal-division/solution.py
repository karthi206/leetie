# ──────────────────────────────────────────────────
# Problem  : 553. Optimal Division
# Difficulty: Medium
# Tags     : Array, Math, Dynamic Programming
# Link     : https://leetcode.com/problems/optimal-division/
# Runtime  : 0 ms (beats 100%)
# Memory   : 19160000 (beats 88%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        n = len(nums)
        if n == 1:
            return str(nums[0])
        elif n == 2:
            return f"{nums[0]}/{nums[1]}"
        else:
            return f"{nums[0]}/({'/'.join(map(str, nums[1:]))})"