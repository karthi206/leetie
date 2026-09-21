# ──────────────────────────────────────────────────
# Problem  : 583. Delete Operation for Two Strings
# Difficulty: Medium
# Tags     : String, Dynamic Programming, Longest Common Subsequence
# Link     : https://leetcode.com/problems/delete-operation-for-two-strings/
# Runtime  : 60 ms (beats 94%)
# Memory   : 19256000 (beats 96%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        if m > n:
            return self.minDistance(word2, word1)

        dp = [0] * (m + 1)

        for i in range(1, n + 1):
            prev = 0

            for j in range(1, m + 1):
                temp = dp[j]

                if word1[i - 1] == word2[j - 1]:
                    dp[j] = 1 + prev
                else:
                    dp[j] = max(dp[j], dp[j - 1])

                prev = temp

        return n + m - 2 * dp[m]