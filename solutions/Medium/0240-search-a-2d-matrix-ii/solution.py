# ──────────────────────────────────────────────────
# Problem  : 240. Search a 2D Matrix II
# Difficulty: Medium
# Tags     : Array, Binary Search, Divide and Conquer, Matrix
# Link     : https://leetcode.com/problems/search-a-2d-matrix-ii/
# Runtime  : 138 ms (beats 77%)
# Memory   : 25588000 (beats 61%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        r = 0
        c = n - 1
        while r <= m - 1 and c >= 0:
            if target == matrix[r][c]:
                return True
            elif target > matrix[r][c]:
                r += 1
            else:
                c -= 1
        return False