# ──────────────────────────────────────────────────
# Problem  : 454. 4Sum II
# Difficulty: Medium
# Tags     : Array, Hash Table
# Link     : https://leetcode.com/problems/4sum-ii/
# Runtime  : 334 ms (beats 78%)
# Memory   : 19332000 (beats 81%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n, hm, res = len(nums1), defaultdict(int), 0

        for i in range(n):
            for j in range(n):
                hm[nums1[i] + nums2[j]] += 1 

        for k in range(n):
            for l in range(n):
                res += hm[0 - (nums3[k] + nums4[l])]

        return res        