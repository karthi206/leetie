# ──────────────────────────────────────────────────
# Problem  : 3193. Count the Number of Inversions
# Difficulty: Hard
# Tags     : Array, Dynamic Programming
# Link     : https://leetcode.com/problems/count-the-number-of-inversions/
# Runtime  : 46 ms (beats 0%)
# Memory   : 19512000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
        requirements = {end + 1: cnt for end, cnt in requirements}
        
        @cache
        def dfs(distinctN: int, inversions: int) -> int:
            """Return the number of permutations of distinctN distinct elements 
            that satisfy the requirements and have exactly 'inversions' inversions.
            """
            if inversions < 0:
                return 0
            if distinctN in requirements and requirements[distinctN] != inversions:
                return 0
            if distinctN == 1:
                return 1 if inversions == 0 else 0
            
            result = 0
            for i in range(1, distinctN + 1):
                inversionsCaused = distinctN - i
                result += dfs(distinctN - 1, inversions - inversionsCaused)
                
            return result
        
        res = dfs(n, requirements[n])
        return res % (10 ** 9 + 7)