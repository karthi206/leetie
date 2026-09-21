# ──────────────────────────────────────────────────
# Problem  : 518. Coin Change II
# Difficulty: Medium
# Tags     : Array, Dynamic Programming, Knapsack Problem, Complete Knapsack
# Link     : https://leetcode.com/problems/coin-change-ii/
# Runtime  : 511 ms (beats 40%)
# Memory   : 65372000 (beats 30%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        
        for i in range(n + 1):
            dp[i][0] = 1
            
        for i in range(1, n + 1):
            for j in range(1, amount + 1):
                if coins[i-1] <= j:
                    dp[i][j] = dp[i][j - coins[i-1]] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
                    
        return dp[n][amount]