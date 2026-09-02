# ──────────────────────────────────────────────────
# Problem  : 215. Kth Largest Element in an Array
# Difficulty: Medium
# Tags     : Array, Divide and Conquer, Sorting, Heap (Priority Queue), Quickselect
# Link     : https://leetcode.com/problems/kth-largest-element-in-an-array/
# Runtime  : 54 ms (beats 84%)
# Memory   : 30988000 (beats 70%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]