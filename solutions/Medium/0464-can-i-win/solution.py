# ──────────────────────────────────────────────────
# Problem  : 464. Can I Win
# Difficulty: Medium
# Tags     : Math, Dynamic Programming, Bit Manipulation, Memoization, Game Theory, Bitmask
# Link     : https://leetcode.com/problems/can-i-win/
# Runtime  : 1495 ms (beats 89%)
# Memory   : 126584000 (beats 62%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= 0:
            return True

        max_possible_sum = (maxChoosableInteger * (maxChoosableInteger + 1)) // 2
        if max_possible_sum < desiredTotal:
            return False
            
        memo = {}
        
        def dfs(mask: int, current_total: int) -> bool:
            if mask in memo:
                return memo[mask]

            for i in range(1, maxChoosableInteger + 1):
                bit = 1 << (i - 1)

                if not (mask & bit):
                    if current_total + i >= desiredTotal or not dfs(mask | bit, current_total + i):
                        memo[mask] = True
                        return True

            memo[mask] = False
            return False
            
        return dfs(0, 0)