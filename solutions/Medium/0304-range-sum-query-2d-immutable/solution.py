# ──────────────────────────────────────────────────
# Problem  : 304. Range Sum Query 2D - Immutable
# Difficulty: Medium
# Tags     : Array, Design, Matrix, Prefix Sum
# Link     : https://leetcode.com/problems/range-sum-query-2d-immutable/
# Runtime  : 112 ms (beats 67%)
# Memory   : 34320000 (beats 13%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.dp=[[0] * (len(matrix[0])+1) for _ in range(len(matrix)+1)]
        
		# calculate prefix sum
        for r in range(len(self.dp)-1):
            for c in range(len(self.dp[0])-1):
                self.dp[r+1][c+1]=matrix[r][c] + self.dp[r][c+1] + self.dp[r+1][c] - self.dp[r][c]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2+1][col2+1] - self.dp[row1][col2+1] - self.dp[row2+1][col1] + self.dp[row1][col1]
                