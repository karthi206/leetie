# ──────────────────────────────────────────────────
# Problem  : 611. Valid Triangle Number
# Difficulty: Medium
# Tags     : Array, Two Pointers, Binary Search, Greedy, Sorting
# Link     : https://leetcode.com/problems/valid-triangle-number/
# Runtime  : 441 ms (beats 91%)
# Memory   : 19332000 (beats 39%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        count = 0

        for i in range(n - 1, -1, -1):
            left, right = 0, i - 1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    count += right - left
                    right -= 1
                else:
                    left += 1
        return count