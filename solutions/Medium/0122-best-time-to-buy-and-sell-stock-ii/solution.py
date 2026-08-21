# ──────────────────────────────────────────────────
# Problem  : 122. Best Time to Buy and Sell Stock II
# Difficulty: Medium
# Tags     : Array, Dynamic Programming, Greedy
# Link     : https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
# Runtime  : 2 ms (beats 67%)
# Memory   : 20292000 (beats 86%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]

        return profit