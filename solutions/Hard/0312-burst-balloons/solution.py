# ──────────────────────────────────────────────────
# Problem  : 312. Burst Balloons
# Difficulty: Hard
# Tags     : Array, Dynamic Programming
# Link     : https://leetcode.com/problems/burst-balloons/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19388000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        nums.insert(0,1)
        nums.append(1)

        def recursive(i, j, memo):
            if i == j:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            max_cost = float('-inf')
            for k in range(i, j):
                curr_cost = nums[i-1] * nums[k] * nums[j]
                left_cost = recursive(i, k, memo)
                right_cost = recursive(k+1, j, memo)
                max_cost = max(max_cost, curr_cost + left_cost + right_cost)
            memo[(i,j)] = max_cost
            return max_cost
        
        memo = {}
        return recursive(1, len(nums)-1, memo)
        