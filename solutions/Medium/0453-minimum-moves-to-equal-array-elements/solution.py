# ──────────────────────────────────────────────────
# Problem  : 453. Minimum Moves to Equal Array Elements
# Difficulty: Medium
# Tags     : Array, Math
# Link     : https://leetcode.com/problems/minimum-moves-to-equal-array-elements/
# Runtime  : 11 ms (beats 31%)
# Memory   : 20612000 (beats 41%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def minMoves(self, nums):
        min_element = min(nums)
        return sum(num - min_element for num in nums)