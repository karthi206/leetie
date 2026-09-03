# ──────────────────────────────────────────────────
# Problem  : 330. Patching Array
# Difficulty: Hard
# Tags     : Array, Greedy
# Link     : https://leetcode.com/problems/patching-array/
# Runtime  : 0 ms (beats 100%)
# Memory   : 19196000 (beats 97%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        miss = 1
        result = 0
        i = 0

        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                result += 1

        return result