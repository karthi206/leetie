# ──────────────────────────────────────────────────
# Problem  : 377. Combination Sum IV
# Difficulty: Medium
# Tags     : Array, Dynamic Programming
# Link     : https://leetcode.com/problems/combination-sum-iv/
# Runtime  : 54 ms (beats 32%)
# Memory   : 19232000 (beats 67%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort() 
        memo = {}
        
        def helper(n):
            if n in memo:
                return memo[n]
            if n == 0:
                return 1
            if n < nums[0]:
                return 0
            
            count = 0
            for num in nums:
                if n - num < 0:
                    break 
                count += helper(n - num)
                
            memo[n] = count
            return count
        
        return helper(target)