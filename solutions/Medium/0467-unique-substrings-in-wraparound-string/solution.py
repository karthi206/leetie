# ──────────────────────────────────────────────────
# Problem  : 467. Unique Substrings in Wraparound String
# Difficulty: Medium
# Tags     : String, Dynamic Programming
# Link     : https://leetcode.com/problems/unique-substrings-in-wraparound-string/
# Runtime  : 95 ms (beats 10%)
# Memory   : 33744000 (beats 8%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    """My Recursive Memoization Solution"""
    def findSubstringInWraproundString(self, s: str) -> int:
        n = len(s)

        def dp(i, memo: dict):
            if i == 0:
                return 1
            if i not in memo:
                if (ord(s[i]) - ord(s[i - 1])) % 26 == 1:
                    memo[i] = dp(i - 1, memo) + 1
                else:
                    memo[i] = 1
            return memo[i]

        memo_dict = {}
        best = {}
        for j in range(n):
            if s[j] not in best:
                best[s[j]] = 0
            best[s[j]] = max(best[s[j]], dp(j, memo_dict))
        return sum(best[i] for i in best)