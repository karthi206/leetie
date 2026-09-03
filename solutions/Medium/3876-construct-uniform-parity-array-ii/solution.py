# ──────────────────────────────────────────────────
# Problem  : 3876. Construct Uniform Parity Array II
# Difficulty: Medium
# Tags     : Array, Math
# Link     : https://leetcode.com/problems/construct-uniform-parity-array-ii/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19356000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        return (min(nums1)&1)==1 or (reduce(or_, nums1)&1)==0