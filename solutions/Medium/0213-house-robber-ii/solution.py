# ──────────────────────────────────────────────────
# Problem  : 213. House Robber II
# Difficulty: Medium
# Tags     : Array, Dynamic Programming
# Link     : https://leetcode.com/problems/house-robber-ii/
# Runtime  : 0 ms (beats 100%)
# Memory   : 19188000 (beats 93%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def rob(self, nums: List[int]) -> int:

        def get_max(nums):
            prev_rob = max_rob = 0

            for cur_val in nums:
                temp = max(max_rob, prev_rob + cur_val)
                prev_rob = max_rob
                max_rob = temp
            
            return max_rob
        
        return max(get_max(nums[:-1]), get_max(nums[1:]), nums[0])