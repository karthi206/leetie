# ──────────────────────────────────────────────────
# Problem  : 287. Find the Duplicate Number
# Difficulty: Medium
# Tags     : Array, Two Pointers, Binary Search, Bit Manipulation, Pigeonhole Principle, Floyd's Cycle Finding Algorithm
# Link     : https://leetcode.com/problems/find-the-duplicate-number/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19408000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)