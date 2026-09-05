# ──────────────────────────────────────────────────
# Problem  : 376. Wiggle Subsequence
# Difficulty: Medium
# Tags     : Array, Dynamic Programming, Greedy
# Link     : https://leetcode.com/problems/wiggle-subsequence/
# Runtime  : 0 ms (beats 100%)
# Memory   : 19236000 (beats 68%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        up_sequence = 0
        down_sequence = 0
        for i in range(n-1):
            if nums[i] > nums[i+1]: 
                up_sequence = down_sequence + 1
            elif nums[i] < nums[i+1]:
                down_sequence = up_sequence + 1
        return 1 + max(up_sequence, down_sequence)