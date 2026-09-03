# ──────────────────────────────────────────────────
# Problem  : 322. Coin Change
# Difficulty: Medium
# Tags     : Array, Dynamic Programming, Breadth-First Search, Knapsack Problem, Complete Knapsack
# Link     : https://leetcode.com/problems/coin-change/
# Runtime  : 513 ms (beats 57%)
# Memory   : 19640000 (beats 53%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_coins = [amount + 1] * (amount + 1)
        min_coins[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    min_coins[i] = min(min_coins[i], 1 + min_coins[i - c])
        
        return min_coins[-1] if min_coins[-1] != amount + 1 else -1