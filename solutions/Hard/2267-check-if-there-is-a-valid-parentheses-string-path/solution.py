# ──────────────────────────────────────────────────
# Problem  : 2267.  Check if There Is a Valid Parentheses String Path
# Difficulty: Hard
# Tags     : Array, Dynamic Programming, Matrix, Bracket Sequences
# Link     : https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/
# Runtime  : 15 ms (beats 84%)
# Memory   : 29468000 (beats 76%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def hasValidPath(self, A: list[list[str]]) -> bool:
        m, n = len(A), len(A[0])

        if ~(m + n) & 1 or A[0][0] == ")" or A[-1][-1] == "(":
            return False

        @cache
        def dfs(i, j, x):
            x += 1 - ((ord(A[i][j]) & 1) << 1)

            if x < 0 or x > m - i + n - j - 1:
                return False

            if i == m - 1 and j == n - 1:
                return x == 0

            return (i < m - 1 and dfs(i + 1, j, x)) or \
                   (j < n - 1 and dfs(i, j + 1, x))

        return dfs(0, 0, 0)