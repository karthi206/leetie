# ──────────────────────────────────────────────────
# Problem  : 164. Maximum Gap
# Difficulty: Medium
# Tags     : Array, Sorting, Bucket Sort, Radix Sort, Pigeonhole Principle
# Link     : https://leetcode.com/problems/maximum-gap/
# Runtime  : 127 ms (beats 96%)
# Memory   : 31948000 (beats 60%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0
        nums.sort()
        maxgap=0
        for i in range (len(nums)-1):
            gap=nums[i+1]-nums[i]
            if gap>maxgap:
                maxgap=gap
        return maxgap
                
        