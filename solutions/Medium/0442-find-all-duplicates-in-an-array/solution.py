# ──────────────────────────────────────────────────
# Problem  : 442. Find All Duplicates in an Array
# Difficulty: Medium
# Tags     : Array, Hash Table, Sorting
# Link     : https://leetcode.com/problems/find-all-duplicates-in-an-array/
# Runtime  : 43 ms (beats 26%)
# Memory   : 29532000 (beats 84%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans =[]
        n=len(nums)
        for x in nums:
            x = abs(x)
            if nums[x-1]<0:
                ans.append(x)
            nums[x-1] *= -1
        return ans