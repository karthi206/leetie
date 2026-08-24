# ──────────────────────────────────────────────────
# Problem  : 1872. Stone Game VIII
# Difficulty: Hard
# Tags     : Array, Math, Dynamic Programming, Minimax, Prefix Sum, Game Theory, Zero-Sum Game
# Link     : https://leetcode.com/problems/stone-game-viii/
# Runtime  : 670 ms (beats 69%)
# Memory   : 33056000 (beats 64%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        for i in range(1, n):
            stones[i] += stones[i - 1]
        best = stones[-1]
        for i in range(n - 2, 0, -1):
            best = max(best, stones[i] - best)
        return best