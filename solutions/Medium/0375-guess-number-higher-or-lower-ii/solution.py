# ──────────────────────────────────────────────────
# Problem  : 375. Guess Number Higher or Lower II
# Difficulty: Medium
# Tags     : Math, Dynamic Programming, Minimax, Game Theory
# Link     : https://leetcode.com/problems/guess-number-higher-or-lower-ii/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19312000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        if n == 1:
            return 1
        starting_index = 1 if n % 2 == 0 else 2
        selected_nums = [i for i in range(starting_index, n, 2)]
        selected_nums_length = len(selected_nums)
        dp = [[0] * selected_nums_length for _ in range(selected_nums_length)]

        for i in range(selected_nums_length):
            dp[i][i] = selected_nums[i]

        for length in range(2, selected_nums_length + 1):
            for i in range(selected_nums_length - length + 1):
                j = i + length - 1
                dp[i][j] = float("inf")
                for k in range(i, j + 1):
                    dp_left = dp[i][k - 1] if k != 0 else 0
                    dp_right = dp[k + 1][j] if k != j else 0
                    dp[i][j] = min(dp[i][j], selected_nums[k] + max(dp_left, dp_right))

        return dp[0][-1]