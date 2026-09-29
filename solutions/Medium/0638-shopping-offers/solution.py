# ──────────────────────────────────────────────────
# Problem  : 638. Shopping Offers
# Difficulty: Medium
# Tags     : Array, Dynamic Programming, Backtracking, Bit Manipulation, Memoization, Bitmask, Knapsack Problem, Complete Knapsack
# Link     : https://leetcode.com/problems/shopping-offers/
# Runtime  : 22 ms (beats 34%)
# Memory   : 19740000 (beats 33%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        p = len(price)

        def dp(curr, memo):
            if all(i == 0 for i in curr):
                return 0
            key = tuple(curr)
            if key not in memo:
                n = len(curr)
                memo[key] = sum(curr[i] * price[i] for i in range(p))
                for offer in special:
                    if all(curr[i] >= offer[i] for i in range(n)):
                        new = [curr[i] - offer[i] for i in range(n)]
                        memo[key] = min(memo[key], offer[-1] + dp(new, memo))
            return memo[key]
        return dp(needs, {})