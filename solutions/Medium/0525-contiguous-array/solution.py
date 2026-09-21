# ──────────────────────────────────────────────────
# Problem  : 525. Contiguous Array
# Difficulty: Medium
# Tags     : Array, Hash Table, Prefix Sum
# Link     : https://leetcode.com/problems/contiguous-array/
# Runtime  : 79 ms (beats 55%)
# Memory   : 25056000 (beats 94%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mp = {}
        sum_val = 0
        max_len = 0
        for i, num in enumerate(nums):
            sum_val += 1 if num == 1 else -1
            if sum_val == 0:
                max_len = i + 1
            elif sum_val in mp:
                max_len = max(max_len, i - mp[sum_val])
            else:
                mp[sum_val] = i
        return max_len