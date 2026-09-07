# ──────────────────────────────────────────────────
# Problem  : 462. Minimum Moves to Equal Array Elements II
# Difficulty: Medium
# Tags     : Array, Math, Sorting
# Link     : https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/
# Runtime  : 7 ms (beats 48%)
# Memory   : 20448000 (beats 51%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        median = nums[len(nums) // 2]
        return sum(abs(num - median) for num in nums)