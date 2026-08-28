# ──────────────────────────────────────────────────
# Problem  : 300. Longest Increasing Subsequence
# Difficulty: Medium
# Tags     : Array, Binary Search, Dynamic Programming, Longest Increasing Subsequence
# Link     : https://leetcode.com/problems/longest-increasing-subsequence/
# Runtime  : 1299 ms (beats 23%)
# Memory   : 19420000 (beats 59%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [1] * n

        ans = 1

        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

            ans = max(ans, dp[i])

        return ans