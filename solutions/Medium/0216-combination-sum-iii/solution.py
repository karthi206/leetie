# ──────────────────────────────────────────────────
# Problem  : 216. Combination Sum III
# Difficulty: Medium
# Tags     : Array, Backtracking
# Link     : https://leetcode.com/problems/combination-sum-iii/
# Runtime  : 0 ms (beats 100%)
# Memory   : 19340000 (beats 34%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def backtrack(start, path, target, k):
            if target == 0 and k == 0:
                res.append(path[:])
                return
            for i in range(start, 10):
                if i > target or k <= 0:
                    break
                path.append(i)
                backtrack(i+1, path, target - i, k - 1)
                path.pop()
        backtrack(1, [], n, k)
        return res