# ──────────────────────────────────────────────────
# Problem  : 540. Single Element in a Sorted Array
# Difficulty: Medium
# Tags     : Array, Binary Search
# Link     : https://leetcode.com/problems/single-element-in-a-sorted-array/
# Runtime  : 0 ms (beats 100%)
# Memory   : 26988000 (beats 63%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = int((left + right)/2)
            if (mid % 2 == 1 and nums[mid - 1] == nums[mid]) or (mid%2 == 0 and nums[mid] == nums[mid + 1]):
                left = mid + 1
            else:
                right = mid
        return nums[left]