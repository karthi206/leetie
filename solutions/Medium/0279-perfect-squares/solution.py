# ──────────────────────────────────────────────────
# Problem  : 279. Perfect Squares
# Difficulty: Medium
# Tags     : Math, Dynamic Programming, Breadth-First Search, Knapsack Problem, Complete Knapsack
# Link     : https://leetcode.com/problems/perfect-squares/
# Runtime  : 174 ms (beats 91%)
# Memory   : 20500000 (beats 25%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import deque

class Solution:
    def numSquares(self, n: int) -> int:
        # 1. VISITED + QUEUE
        visited = {n}
        queue = deque([(n, 0)])
        
        # 2. WHILE QUEUE
        while queue:
            to_sum, p_sqrs = queue.popleft()

            # 3. FOR NEIGHBORS, CHECK, ADD TO VISITED + QUEUE
            i = 1
            while i**2 <= to_sum:
                remainder = to_sum - i**2
                
                # CHECK
                if remainder == 0:
                    return p_sqrs + 1
                
                # ADD TO VISITED + QUEUE
                if remainder not in visited:
                    visited.add(remainder)
                    queue.append((remainder, p_sqrs + 1))
                
                i += 1