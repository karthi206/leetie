# ──────────────────────────────────────────────────
# Problem  : 581. Shortest Unsorted Continuous Subarray
# Difficulty: Medium
# Tags     : Array, Two Pointers, Stack, Greedy, Sorting, Monotonic Stack
# Link     : https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
# Runtime  : 4 ms (beats 90%)
# Memory   : 20556000 (beats 51%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        greatest = float('-inf')
        smallest = float('inf')
        left = right = 0
        for i in range(n):
            if nums[i] >= greatest:
                greatest = nums[i]
            else:
                right = i

        for i in range(n - 1, -1, -1):
            if nums[i] <= smallest:
                smallest = nums[i]
            else:
                left = i

        return right - left + 1 if right != 0 or left != 0 else 0