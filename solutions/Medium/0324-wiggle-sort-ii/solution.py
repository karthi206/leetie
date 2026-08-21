# ──────────────────────────────────────────────────
# Problem  : 324. Wiggle Sort II
# Difficulty: Medium
# Tags     : Array, Divide and Conquer, Greedy, Sorting, Quickselect
# Link     : https://leetcode.com/problems/wiggle-sort-ii/
# Runtime  : 7 ms (beats 66%)
# Memory   : 20664000 (beats 44%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        n = len(nums)
        nums.sort()
        mid = (n - 1) // 2
        nums[::2], nums[1::2] = nums[mid::-1], nums[:mid:-1]