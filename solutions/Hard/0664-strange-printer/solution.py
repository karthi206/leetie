# ──────────────────────────────────────────────────
# Problem  : 664. Strange Printer
# Difficulty: Hard
# Tags     : String, Dynamic Programming
# Link     : https://leetcode.com/problems/strange-printer/
# Runtime  : 167 ms (beats 72%)
# Memory   : 19268000 (beats 95%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[-1] * n for _ in range(n)]
        return self.Util(0, n - 1, s, dp)

    def Util(self, i: int, j: int, s: str, dp: list) -> int:
        if i > j:
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        first_letter = s[i]
        # If the current character is not repeated in the rest of the string
        answer = 1 + self.Util(i + 1, j, s, dp)
        for k in range(i + 1, j + 1):
            # If repeated then update the answer
            if s[k] == first_letter:
                # Splitting from i -> k - 1 (remove the last character)
                # and from k + 1 -> j             
                better_answer = self.Util(i, k - 1, s, dp) + self.Util(k + 1, j, s, dp)
                answer = min(answer, better_answer)
        dp[i][j] = answer
        return answer