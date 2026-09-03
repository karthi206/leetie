# ──────────────────────────────────────────────────
# Problem  : 322. Coin Change
# Difficulty: Medium
# Tags     : Array, Dynamic Programming, Breadth-First Search, Knapsack Problem, Complete Knapsack
# Link     : https://leetcode.com/problems/coin-change/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19324000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount < 0:
            return -1
        if amount == 0:
            return 0
        
        min_count = float('inf')
        
        for coin in coins:
            res = self.coinChange(coins, amount - coin)
            if res != -1:
                min_count = min(min_count, 1 + res)
                
        return min_count if min_count != float('inf') else -1