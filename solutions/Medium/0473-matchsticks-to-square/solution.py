# ──────────────────────────────────────────────────
# Problem  : 473. Matchsticks to Square
# Difficulty: Medium
# Tags     : Array, Dynamic Programming, Backtracking, Bit Manipulation, Bitmask
# Link     : https://leetcode.com/problems/matchsticks-to-square/
# Runtime  : 429 ms (beats 54%)
# Memory   : 22604000 (beats 15%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        matchsticks.sort(reverse=True)
        n = len(matchsticks)
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        side = total // 4

        def dp(used, curr, memo: dict):
            if curr > side:
                return False
            if curr == side:
                return dp(used, 0, memo)
            if used == (1 << n) - 1:
                return curr == 0

            if (used, curr) not in memo:
                for i in range(n):
                    if not (used & (1 << i)):
                        if dp(used | (1 << i), curr + matchsticks[i], memo):
                            memo[(used, curr)] = True
                            return True
            memo[(used, curr)] = False
            return memo[(used, curr)]
        return dp(0, 0, {})