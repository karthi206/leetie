# ──────────────────────────────────────────────────
# Problem  : 494. Target Sum
# Difficulty: Medium
# Tags     : Array, Dynamic Programming, Backtracking, Knapsack Problem, 0-1 Knapsack
# Link     : https://leetcode.com/problems/target-sum/
# Runtime  : 15 ms (beats 98%)
# Memory   : 19172000 (beats 98%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)

        if total < abs(target):
            return 0

        if (total + target) % 2 != 0:
            return 0

        tar = (total + target) // 2

        dp = [0] * (tar + 1)
        dp[0] = 1

        for num in nums:
            for s in range(tar, num - 1, -1):
                dp[s] += dp[s - num]

        return dp[tar]