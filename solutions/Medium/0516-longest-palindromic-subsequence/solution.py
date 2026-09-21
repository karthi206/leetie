# ──────────────────────────────────────────────────
# Problem  : 516. Longest Palindromic Subsequence
# Difficulty: Medium
# Tags     : String, Dynamic Programming
# Link     : https://leetcode.com/problems/longest-palindromic-subsequence/
# Runtime  : 1311 ms (beats 19%)
# Memory   : 44444000 (beats 35%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        rev = s[::-1]
        n = len(s)
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i-1] == rev[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    
        return dp[n][n]