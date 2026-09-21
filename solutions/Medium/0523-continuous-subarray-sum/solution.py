# ──────────────────────────────────────────────────
# Problem  : 523. Continuous Subarray Sum
# Difficulty: Medium
# Tags     : Array, Hash Table, Math, Prefix Sum, Pigeonhole Principle
# Link     : https://leetcode.com/problems/continuous-subarray-sum/
# Runtime  : 51 ms (beats 69%)
# Memory   : 39672000 (beats 25%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_cache = {0:-1}
        remainder = 0
        for i in range(len(nums)):
            remainder += nums[i]
            remainder %=k
            if remainder not in remainder_cache:
                remainder_cache[remainder] = i
            elif i - remainder_cache[remainder] >=2:
                return True
        return False
        