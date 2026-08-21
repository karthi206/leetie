# ──────────────────────────────────────────────────
# Problem  : 123. Best Time to Buy and Sell Stock III
# Difficulty: Hard
# Tags     : Array, Dynamic Programming
# Link     : https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
# Runtime  : 1861 ms (beats 5%)
# Memory   : 151384000 (beats 9%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        def solve(i, capacity, buy, memo):
            if capacity == 0 or i == n:
                return 0

            if (i, capacity, buy) in memo:
                return memo[(i, capacity, buy)]

            if buy:
                memo[(i, capacity, buy)] = max(
                    -prices[i] + solve(i + 1, capacity, 0, memo),
                    solve(i + 1, capacity, 1, memo)   
                )
            else:
                memo[(i, capacity, buy)] = max(
                    prices[i] + solve(i + 1, capacity - 1, 1, memo),
                    solve(i + 1, capacity, 0, memo)
                )

            return memo[(i, capacity, buy)]   

        return solve(0, 2, 1, {})