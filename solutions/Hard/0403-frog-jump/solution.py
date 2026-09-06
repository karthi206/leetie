# ──────────────────────────────────────────────────
# Problem  : 403. Frog Jump
# Difficulty: Hard
# Tags     : Array, Dynamic Programming
# Link     : https://leetcode.com/problems/frog-jump/
# Runtime  : 123 ms (beats 33%)
# Memory   : 21004000 (beats 81%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        dp = {stone : set() for stone in stones}
        dp[0] = {0}

        for stone in stones:
            for jump in dp[stone]:
                for jump_distance in [jump - 1, jump, jump + 1]:
                    if jump_distance > 0 and stone + jump_distance in dp:
                        dp[stone + jump_distance].add(jump_distance)
        
        return len(dp[stones[-1]]) > 0