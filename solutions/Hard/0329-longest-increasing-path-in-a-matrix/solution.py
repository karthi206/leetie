# ──────────────────────────────────────────────────
# Problem  : 329. Longest Increasing Path in a Matrix
# Difficulty: Hard
# Tags     : Array, Dynamic Programming, Depth-First Search, Breadth-First Search, Graph Theory, Topological Sort, Memoization, Matrix, Directed Acyclic Graph
# Link     : https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
# Runtime  : 109 ms (beats 79%)
# Memory   : 21952000 (beats 69%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[-1] * n for _ in range(m)]

        def dfs(i, j, prevVal):
            if i < 0 or j < 0 or i >= m or j >= n or matrix[i][j] <= prevVal:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            val = matrix[i][j]
            up = 1 + dfs(i-1, j, val)
            down = 1 + dfs(i+1, j, val)
            left = 1 + dfs(i, j-1, val)
            right = 1 + dfs(i, j+1, val)
            dp[i][j] = max(up, down, left, right)
            return dp[i][j]

        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j, -1))
        return ans